#!/usr/bin/env python3
"""Sends an Android App Bundle to a track of Google Play, through its
Developer API (androidpublisher v3), as a service account - nobody opens Play
Console for it (panorun-android.yml; the emulator's SPEC section 9.2):

    play-upload.py PACKAGE BUNDLE --track alpha --name 0.1.19 --notes notes.txt

One edit: the bundle uploaded, the track's release set to it - completed, for
everyone on the track, with the notes in English - and committed, which sends
it for review as Publishing overview's "Send changes for review" does. The
deobfuscation map and the native debug symbols go in the bundle itself
(BUNDLE-METADATA), so nothing else is uploaded.

The service account's key - its JSON - is in the environment, as
PLAY_SERVICE_ACCOUNT_JSON; in Play Console the account has the app's release
rights (Users and permissions). Needs google-auth and requests."""

from __future__ import annotations

import argparse
import json
import os
import sys

from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

API = "https://androidpublisher.googleapis.com/androidpublisher/v3/applications"
UPLOAD = "https://androidpublisher.googleapis.com/upload/androidpublisher/v3/applications"
SCOPE = "https://www.googleapis.com/auth/androidpublisher"
#: Google Play's longest "What's new".
NOTES_MOST = 500


def fail(what, response):
    sys.exit(f"::error::Google Play, {what}: {response.status_code} {response.text[:2000]}")


def answer(response, what):
    if response.status_code >= 300:
        fail(what, response)
    return response.json() if response.content else {}


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("package")
    parser.add_argument("bundle")
    parser.add_argument("--track", default="alpha")
    parser.add_argument("--name", required=True, help="the release's name: the version")
    parser.add_argument("--notes", help="a file of what is new, in English")
    args = parser.parse_args()

    key = os.environ.get("PLAY_SERVICE_ACCOUNT_JSON")
    if not key:
        sys.exit("::error::No PLAY_SERVICE_ACCOUNT_JSON")
    notes = ""
    if args.notes:
        with open(args.notes, encoding="utf-8") as handle:
            notes = handle.read().strip()
    if len(notes) > NOTES_MOST:
        sys.exit(f"::error::What's new is {len(notes)} characters: Google Play takes {NOTES_MOST}")

    credentials = service_account.Credentials.from_service_account_info(
        json.loads(key), scopes=[SCOPE])
    session = AuthorizedSession(credentials)
    app = f"{API}/{args.package}"
    edit = answer(session.post(f"{app}/edits", json={}), "opening an edit")["id"]

    # The bundle, in one resumable upload: Google Play works it over before it
    # answers, which takes a minute or two for one of 30 MB.
    size = os.path.getsize(args.bundle)
    start = session.post(f"{UPLOAD}/{args.package}/edits/{edit}/bundles",
                         params={"uploadType": "resumable"},
                         headers={"X-Upload-Content-Type": "application/octet-stream",
                                  "X-Upload-Content-Length": str(size)})
    if start.status_code >= 300 or "Location" not in start.headers:
        fail("starting the bundle's upload", start)
    with open(args.bundle, "rb") as handle:
        bundle = answer(session.put(start.headers["Location"], data=handle,
                                    headers={"Content-Type": "application/octet-stream"},
                                    timeout=1800), "uploading the bundle")
    code = bundle["versionCode"]
    print(f"bundle uploaded: version code {code}, SHA-256 {bundle.get('sha256', '?')}")

    release = {"name": args.name, "versionCodes": [str(code)], "status": "completed"}
    if notes:
        release["releaseNotes"] = [{"language": "en-US", "text": notes}]
    answer(session.put(f"{app}/edits/{edit}/tracks/{args.track}",
                       json={"track": args.track, "releases": [release]}),
           f"setting the track {args.track}")

    committed = session.post(f"{app}/edits/{edit}:commit")
    if committed.status_code >= 300 and "changesNotSentForReview" in committed.text:
        # Google Play will not send this edit for review by itself - changes
        # waiting in Play Console that need a person: committed all the same,
        # to be sent from Publishing overview.
        committed = session.post(f"{app}/edits/{edit}:commit",
                                 params={"changesNotSentForReview": "true"})
        answer(committed, "committing")
        print(f"::warning::{args.name} is on the track {args.track}, not sent for review: "
              "Play Console, Publishing overview, Send changes for review")
        return
    answer(committed, "committing")
    print(f"{args.name} ({code}) on the track {args.track}, sent for review")


if __name__ == "__main__":
    main()
