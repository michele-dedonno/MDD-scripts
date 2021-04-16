#! /bin/bash

# Script to verify a PGP-signed message against its public key

# Usage: ./verify_msg.sh <pgp-public-key> <message-file>

#set -e

# Check input parameters

if (( $# != 2 )); then

        echo "[-] Illegal number of parameters."

        echo "[+] Usage: $0 <pgp-public-key> <signed-message>"

        exit 1

fi

# Import the pub key

echo "[+] Importing the key..."

echo "[$] gpg --import $1"

gpg --import $1

fingerprint=$(gpg --show-key $1 | grep fingerprint | awk -F '= ' '{print $2;}')

echo $fingerprint

# Verify the message

echo "[+] Verifying the message..."

echo "[$] gpg --verify $2"

gpg --verify $2

# Delete the imported key

echo "[+] Deleting the key..."

echo "[$] gpg --batch --delete-keys '$fingerprint'"

gpg --batch --delete-keys "$fingerprint"

echo "[+] Finished".

# List available keys

#echo "[+] Currently available public keys:"

#gpg -k --with-colons
