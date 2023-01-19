# Passphrase Generator

Python script to create passphrases of various length, including alpha numeric and special characters.

# Usage
```bash
usage: pass-gen.py [-h] [-w WORDS] [-n] [-s SEPARATOR] [-f FILE] [-v]

Generate a strong passphrase.

options:
  -h, --help            show this help message and exit
  -w WORDS, --words WORDS
                        number of words
  -n, --numeric         add a number at each word
  -s SEPARATOR, --separator SEPARATOR
                        words separator
  -f FILE, --file FILE  path to dictionary
  -v, --verbose         verbose output
```

Example:
```bash
$ python3 pass-gen.py -f ./my_eff_large_wordlist.txt -n 10 -v

Deplete4-Surgery2-Species8-Thesis1-Placidly8-Glitter2-Mashing0-Tidiness6-Hastiness9-Baking4

Number of words:    10
Number of letters:  91
```

# Wordlists
The script uses by default the [EFF large wordlist](./my_eff_large_wordlist.txt).

However, additional wordlists can be found at https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases.

# Credit
This script is inspired from the zwolbers script (https://github.com/zwolbers/passphrase-generator/).
