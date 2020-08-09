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
#     Bash script that implements a basic IP sweep scan aimed at determining 
#     which IP addresses are live in the /24 subnet provided as input.
# 	
#     Example of usage:
#	$ ./ipsweep.sh 192.168.1 > hostlist.txt	
#	$  for ip in $(cat hostlist.txt); do nmap -sS -sU -T4 -A -v $ip; done
#
#     This script is inspired from the Udemy course "Practical Ethical 
#     Hacking - The Complete Course" taught by Heath Adams.
#   % ====================================================================== %
# 

# TODO: to check that the input IP corresponds to 3 valids IPv6 octets

if [ "$1" == "" ]
then
	echo -e "Error:\t Missing subnet IP.";
	echo -e "Usage:\t $0 <Subnet /24 IP>. Example: $0 192.168.1";
	exit 1;
fi
# Remember:
# 	$ ping -c 1 192.168.1.101
# 	PING 192.168.1.101 (192.168.1.101) 56(84) bytes of data.
# 	64 bytes from 192.168.1.101: icmp_seq=1 ttl=128 time=0.125 ms
#
# 	--- 192.168.1.101 ping statistics ---
# 	1 packets transmitted, 1 received, 0% packet loss, time 0ms
# 	rtt min/avg/max/mdev = 0.125/0.125/0.125/0.000 ms
for host in `seq 254`; do
	# $1: first user input
	# grep: select only lines where there is the ping response
	# cut: take the 4th field, after splitting the input string at each space
       	# tr: remove the final ":"
	# &: run the successive ping without waiting for the result of the previous one
	ping -c 1 $1.$host | grep "ttl" | cut -d " " -f 4 | tr -d ":" &
done
