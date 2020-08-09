#!/bin/bash
# Simple IP sweep script that checks hosts online in the /24 subnet provided as input


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
