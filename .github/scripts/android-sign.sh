#!/usr/bin/env bash
# Signs Panorun's Android app here on GitHub (panorun-android.yml), as the
# emulator's android/sign.sh does on the computer that builds it: Google Play's
# bundle with jarsigner, the APK - its uncompressed libraries aligned to 16 KB
# pages first - with apksigner. Nobody types the key's password: the key is the
# secret PANORUN_ANDROID_SIGNING, JSON - "keystore" (the PKCS #12 file, base64)
# and "password" (the emulator's android/set-signing-secret.ps1 puts it there).
#
# Only Panorun's key signs - its certificate's SHA-256 is ANDROID_CERTIFICATE:
# an APK signed with another would not install over Panorun, and Google Play
# would refuse a bundle not signed with its upload key.
#
#     android-sign.sh UNSIGNED.aab UNSIGNED.apk OUTDIR VERSION
#
# Writes OUTDIR/Panorun-VERSION.aab and OUTDIR/Panorun-VERSION.apk. TOOLS is
# Android's build-tools (zipalign, apksigner); keytool and jarsigner are on the
# path.
set -euo pipefail

aab=$1 apk=$2 out=$3 version=$4
: "${PANORUN_ANDROID_SIGNING:?no PANORUN_ANDROID_SIGNING}" "${ANDROID_CERTIFICATE:?}" "${TOOLS:?}"
mkdir -p "$out"
work=$(mktemp -d)
trap 'rm -rf "$work"; unset PANORUN_STOREPASS' EXIT
keystore="$work/panorun.p12"

PANORUN_STOREPASS=$(python3 - "$keystore" <<'EOF'
import base64
import json
import os
import sys

key = json.loads(os.environ["PANORUN_ANDROID_SIGNING"])
with open(sys.argv[1], "wb") as handle:
    handle.write(base64.b64decode(key["keystore"]))
print(key["password"])
EOF
)
if [ "${GITHUB_ACTIONS:-}" = true ]; then
  # Never in the log, whatever prints it.
  echo "::add-mask::$PANORUN_STOREPASS"
fi
export PANORUN_STOREPASS

listing=$(keytool -list -v -keystore "$keystore" -storetype PKCS12 -storepass:env PANORUN_STOREPASS)
alias=$(echo "$listing" | sed -n 's/^Alias name: //p' | head -1)
digest=$(echo "$listing" | sed -n 's/^[[:space:]]*SHA256: //p' | head -1 | tr -d ':' | tr 'A-F' 'a-f')
if [ -z "$alias" ]; then
  echo "::error::No key in PANORUN_ANDROID_SIGNING's keystore"
  exit 1
fi
if [ "$digest" != "$ANDROID_CERTIFICATE" ]; then
  echo "::error::PANORUN_ANDROID_SIGNING is not Panorun's key: its certificate is $digest, Panorun's $ANDROID_CERTIFICATE"
  exit 1
fi
echo "signing with the key \"$alias\", certificate SHA-256 $digest"

# A bundle is a jar to Google Play: jarsigner signs it.
jarsigner -keystore "$keystore" -storetype PKCS12 \
  -storepass:env PANORUN_STOREPASS -keypass:env PANORUN_STOREPASS \
  -sigalg SHA256withRSA -digestalg SHA-256 \
  -signedjar "$out/Panorun-$version.aab" "$aab" "$alias" > /dev/null
jarsigner -verify "$out/Panorun-$version.aab" | tail -1

# An APK Android installs needs apksigner's signatures, and its uncompressed
# libraries aligned to 16 KB pages before them.
"$TOOLS/zipalign" -f -P 16 4 "$apk" "$work/aligned.apk"
"$TOOLS/apksigner" sign --ks "$keystore" --ks-type PKCS12 \
  --ks-pass env:PANORUN_STOREPASS --key-pass env:PANORUN_STOREPASS \
  --ks-key-alias "$alias" --out "$out/Panorun-$version.apk" "$work/aligned.apk"
signed=$("$TOOLS/apksigner" verify --print-certs "$out/Panorun-$version.apk" \
         | sed -n 's/.*certificate SHA-256 digest: //p' | head -1)
if [ "$signed" != "$ANDROID_CERTIFICATE" ]; then
  echo "::error::The APK came out signed by $signed, not Panorun's key"
  exit 1
fi
echo "apk verified: certificate SHA-256 $signed"
ls -l "$out"
