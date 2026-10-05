#!/usr/bin/env python3
"""update.json for Cam2You's desktop apps, signed (cam2you's SPEC §13.1).

The release job of cam2you-release.yml runs it on the release's files before
they are uploaded:

    update-manifest.py dist --tag cam2you-v0.1.4 --version 0.1.4 --montage-version 0.1.1

It lists every desktop file in the folder (Windows' installers, Linux's
AppImages, macOS's disk images) and writes the folder's update.json:

    {
      "schema": 1,
      "tag": "cam2you-v0.1.4",
      "version": "0.1.4",           Cam2You's version
      "montage_version": "0.1.1",
      "min_version": "0.0.0",       the oldest Cam2You that may update itself to it
      "published": "2026-10-05T12:00:00Z",
      "expires": "2027-10-05T12:00:00Z",
      "files": [{"name": "Cam2You-Only-Setup-0.1.4.exe", "app": "Cam2You",
                 "platform": "windows", "version": "0.1.4",
                 "url": "https://github.com/<repository>/releases/download/<tag>/<name>",
                 "sha256": "...", "size": 123}, ...]
    }

The apps refuse it once it has expired (--days after now, 365 by default): a
new release, or this script run again on the release's files and the new
update.json and signature uploaded with `gh release upload --clobber`, renews it.

Then it signs update.json in minisign's format, as `minisign -Sm update.json`
does (Ed25519 over the file's BLAKE2b-512, and over that signature with the
trusted comment), into update.json.minisig. The key is the environment
variable UPDATE_SIGNING_KEY: an unencrypted minisign secret key
(`minisign -G -W`), the key file's text. Anyone can check the result:

    minisign -Vm update.json -P <public key>

Without the key only update.json is written, which the apps refuse; with
--require-key (a published release) that is an error. Signing uses Python's
`cryptography` package when it is there, else the openssl command (1.1.1 or
newer); --openssl uses the command anyway.
"""

import argparse
import base64
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.parse

VERSION = r'(\d+(?:\.\d+)*)'

# The release's desktop files (the release file names agreed between the
# workflows): platform, pattern giving the app and its version.
DESKTOP_FILES = [
    ('windows', re.compile(rf'^(Cam2You)(?:-Web|-Only)?-Setup-{VERSION}\.exe$')),
    ('windows', re.compile(rf'^(Montage)-Setup-{VERSION}\.exe$')),
    ('linux', re.compile(rf'^(Cam2You|Montage)-{VERSION}-x86_64\.AppImage$')),
    ('macos', re.compile(rf'^(Cam2You|Montage)-{VERSION}\.dmg$')),
]

MANIFEST = 'update.json'
SIGNATURE = 'update.json.minisig'

# PKCS #8 for an Ed25519 key, before its 32-byte seed (RFC 8410).
PKCS8_ED25519 = bytes.fromhex('302e020100300506032b657004220420')


def fail(message):
    print(f'::error::{message}', file=sys.stderr)
    sys.exit(1)


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def desktop_files(folder, tag, repository, versions):
    files = []
    for name in sorted(os.listdir(folder)):
        for platform, pattern in DESKTOP_FILES:
            match = pattern.match(name)
            if not match:
                continue
            app, version = match.group(1), match.group(2)
            if version != versions[app]:
                fail(f'{name} is not {app} {versions[app]}, the version of this release')
            path = os.path.join(folder, name)
            files.append({
                'name': name,
                'app': app,
                'platform': platform,
                'version': version,
                'url': f'https://github.com/{repository}/releases/download/{tag}/{urllib.parse.quote(name)}',
                'sha256': sha256(path),
                'size': os.path.getsize(path),
            })
            break
    return files


def secret_key(text):
    """The key number, seed and public key of an unencrypted minisign secret key."""
    lines = [l.strip() for l in text.strip().splitlines() if l.strip() and not l.startswith('untrusted comment:')]
    try:
        raw = base64.b64decode(lines[-1], validate=True)
    except Exception:
        fail('UPDATE_SIGNING_KEY is not a minisign secret key (the text of the file minisign -G -W writes)')
    # sig_alg "Ed", kdf_alg, chk_alg "B2", salt (32), opslimit (8), memlimit (8),
    # then key number (8), secret key (seed and public key, 64), checksum (32).
    if len(raw) != 158 or raw[0:2] != b'Ed' or raw[4:6] != b'B2':
        fail('UPDATE_SIGNING_KEY is not a minisign secret key (the text of the file minisign -G -W writes)')
    if raw[2:4] != b'\0\0':
        fail('UPDATE_SIGNING_KEY is protected by a password: make the key with minisign -G -W')
    keynum, secret = raw[54:62], raw[62:126]
    return keynum, secret[:32], secret[32:]


class Ed25519:
    """Signs with a 32-byte seed: with `cryptography`, or the openssl command."""

    def __init__(self, seed, use_openssl=False):
        self.seed = seed
        self.key = None
        if not use_openssl:
            try:
                from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
                self.key = Ed25519PrivateKey.from_private_bytes(seed)
            except ImportError:
                pass

    def public_key(self):
        if self.key:
            from cryptography.hazmat.primitives import serialization
            return self.key.public_key().public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
        with tempfile.TemporaryDirectory() as tmp:
            der = self._openssl(tmp, ['pkey', '-in', self._pem(tmp), '-pubout', '-outform', 'DER'])
        return der[-32:]

    def sign(self, message):
        if self.key:
            return self.key.sign(message)
        with tempfile.TemporaryDirectory() as tmp:
            data = os.path.join(tmp, 'message')
            with open(data, 'wb') as f:
                f.write(message)
            return self._openssl(tmp, ['pkeyutl', '-sign', '-inkey', self._pem(tmp), '-rawin', '-in', data])

    def verify(self, public_key, signature, message):
        try:
            from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
        except ImportError:
            return self._openssl_verify(public_key, signature, message)
        try:
            Ed25519PublicKey.from_public_bytes(public_key).verify(signature, message)
            return True
        except Exception:
            return False

    def _pem(self, tmp):
        path = os.path.join(tmp, 'key.pem')
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, 'w') as f:
            f.write('-----BEGIN PRIVATE KEY-----\n')
            f.write(base64.b64encode(PKCS8_ED25519 + self.seed).decode() + '\n')
            f.write('-----END PRIVATE KEY-----\n')
        return path

    @staticmethod
    def _openssl(tmp, arguments):
        out = os.path.join(tmp, 'out')
        result = subprocess.run(['openssl', *arguments, '-out', out], capture_output=True)
        if result.returncode != 0:
            fail(f'openssl {arguments[0]} failed: {result.stderr.decode(errors="replace").strip()}')
        with open(out, 'rb') as f:
            return f.read()

    @staticmethod
    def _openssl_verify(public_key, signature, message):
        # SubjectPublicKeyInfo for an Ed25519 key, before its 32 bytes.
        spki = bytes.fromhex('302a300506032b6570032100') + public_key
        with tempfile.TemporaryDirectory() as tmp:
            paths = {}
            for name, data in (('pub.der', spki), ('sig', signature), ('message', message)):
                paths[name] = os.path.join(tmp, name)
                with open(paths[name], 'wb') as f:
                    f.write(data)
            result = subprocess.run(['openssl', 'pkeyutl', '-verify', '-pubin', '-keyform', 'DER', '-inkey', paths['pub.der'],
                                     '-rawin', '-in', paths['message'], '-sigfile', paths['sig']], capture_output=True)
            return result.returncode == 0


def sign(path, key_text, use_openssl=False):
    """minisign's signature of the file at [path], prehashed (ED)."""
    keynum, seed, public_key = secret_key(key_text)
    signer = Ed25519(seed, use_openssl)
    if signer.public_key() != public_key:
        fail('UPDATE_SIGNING_KEY is damaged: its public half does not belong to its secret half')
    with open(path, 'rb') as f:
        digest = hashlib.blake2b(f.read(), digest_size=64).digest()
    signature = signer.sign(digest)
    trusted = f'timestamp:{int(time.time())}\tfile:{os.path.basename(path)}\thashed'
    global_signature = signer.sign(signature + trusted.encode())
    # Checked before it is published: the apps must accept it.
    if not (signer.verify(public_key, signature, digest)
            and signer.verify(public_key, global_signature, signature + trusted.encode())):
        fail('The signature of update.json does not verify')
    key_id = keynum[::-1].hex().upper()
    return key_id, (
        f'untrusted comment: signature from the Cam2You update key {key_id}\n'
        f'{base64.b64encode(b"ED" + keynum + signature).decode()}\n'
        f'trusted comment: {trusted}\n'
        f'{base64.b64encode(global_signature).decode()}\n'
    )


def main():
    parser = argparse.ArgumentParser(description='Writes and signs update.json for the desktop files of a Cam2You release.')
    parser.add_argument('folder', help="the release's files")
    parser.add_argument('--tag', required=True, help='the release tag, cam2you-v<version>')
    parser.add_argument('--version', required=True, help="Cam2You's version")
    parser.add_argument('--montage-version', required=True, help="Montage's version")
    parser.add_argument('--min-version', default='0.0.0', help='the oldest Cam2You that may update itself to this one')
    parser.add_argument('--days', type=int, default=365, help='how long the apps accept it')
    parser.add_argument('--repository', default=os.environ.get('GITHUB_REPOSITORY') or 'TIE-Channel/tie-games-com')
    parser.add_argument('--now', help='the time it is made (ISO 8601; tests)')
    parser.add_argument('--require-key', action='store_true', help='fail without UPDATE_SIGNING_KEY')
    parser.add_argument('--openssl', action='store_true', help='sign with the openssl command')
    args = parser.parse_args()

    now = (datetime.datetime.fromisoformat(args.now.replace('Z', '+00:00')) if args.now
           else datetime.datetime.now(datetime.timezone.utc)).replace(microsecond=0)
    stamp = lambda t: t.astimezone(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    files = desktop_files(args.folder, args.tag, args.repository,
                          {'Cam2You': args.version, 'Montage': args.montage_version})
    manifest = {
        'schema': 1,
        'tag': args.tag,
        'version': args.version,
        'montage_version': args.montage_version,
        'min_version': args.min_version,
        'published': stamp(now),
        'expires': stamp(now + datetime.timedelta(days=args.days)),
        'files': files,
    }
    path = os.path.join(args.folder, MANIFEST)
    with open(path, 'w', newline='\n') as f:
        json.dump(manifest, f, indent=2)
        f.write('\n')
    print(f'{MANIFEST}: {len(files)} desktop files, until {manifest["expires"]}')
    for entry in files:
        print(f'  {entry["platform"]:8} {entry["name"]}')

    key = os.environ.get('UPDATE_SIGNING_KEY', '')
    signature = os.path.join(args.folder, SIGNATURE)
    if os.path.exists(signature):
        os.remove(signature)
    if not key.strip():
        if args.require_key:
            fail('No UPDATE_SIGNING_KEY: a published release needs a signed update.json, or the desktop apps would not update from it')
        print(f'::warning::No UPDATE_SIGNING_KEY: {MANIFEST} is not signed, and the apps will not update from it')
        return
    key_id, text = sign(path, key, args.openssl)
    with open(signature, 'w', newline='\n') as f:
        f.write(text)
    print(f'{SIGNATURE}: signed with key {key_id}')


if __name__ == '__main__':
    main()
