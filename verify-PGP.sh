#!/bin/bash

#   Copyright (C) 2021 Michele De Donno

#   % ============================== LICENSE ============================== %
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>
#   % ====================================================================== %


#   % ======================= DESCRIPTION AND USAGE ======================= &
#     Bash script that verifies a PGP-signed message against its public key.
#     
#     Usage: 
#       $ ./verify-PGP.sh <pgp-public-key> <message-file>
#
#   % ====================================================================== %
# 


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
