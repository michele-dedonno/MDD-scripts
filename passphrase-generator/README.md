# Passphrase Generator

Python script to create passphrases of various length, including alpha numeric and special characters.

# Usage

`python3 pass-gen.py [-h] [-n NUM] [-s SEPARATOR] [-f FILE] [-v]`

Example:
`$ python3 pass-gen.py -f ./my_eff_large_wordlist.txt -n 10 -v`

# Wordlists
The script uses by default the [EFF large wordlist](./my_eff_large_wordlist.txt).

However, additional wordlists can be found at https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases.

# Credit
This script is inspired from the zwolbers script (https://github.com/zwolbers/passphrase-generator/).
