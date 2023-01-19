#! /bin/python3

#   Copyright (C) 2023 Michele De Donno

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
#    Python script to create passphrases. 
#     Usage: 
#      python3 pass-gen.py [-h] [-n NUM] [-s SEPARATOR] [-f FILE] [-v]
#     Example of usage:
#		    $ python3 pass-gen.py -f ./my_eff_large_wordlist.txt -n 10 -v
#
#     This script is inspired from the zwolbers script (https://github.com/zwolbers/passphrase-generator/).
#     Wordlists can be found at https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases.
#   % ====================================================================== %
#
import argparse
import secrets



parser = argparse.ArgumentParser(description = 'Generate a Passphrase')

parser.add_argument('-n', '--num', default = 6, type = int, help = 'number of words')
parser.add_argument('-s', '--separator', default = '-', type = str, help = 'words separator')
parser.add_argument('-f', '--file', default = 'my_eff_large_wordlist.txt', help = 'path to dictionary')
parser.add_argument('-v', '--verbose', action = 'store_true', help = 'verbose output')

args = parser.parse_args()

with open(args.file) as f:
	words = [word.strip() for word in f]
	separator = args.separator
	passphrase = ''.join([secrets.choice(words),str(secrets.randbelow(10))])
	for i in range(args.num-1):
		password = ''.join([secrets.choice(words),str(secrets.randbelow(10))])
		passphrase = separator.join([passphrase, password])

if args.verbose:
	print()
	print(passphrase)
	print()
	print('Number of words:    ' + str(args.num))
	print('Number of letters:  ' + str(len(passphrase)))

else:
	print(password)
