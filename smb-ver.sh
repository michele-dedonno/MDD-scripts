#!/bin/sh

# Author: rewardone
# Description:
#   Requires root or enough permissions to use tcpdump.
#   It will listen for the first 7 packets of a null login
#   and grab the SMB Version
# Notes:
#   It will sometimes not capture or will print multiple
#   lines. It nay need to run a second time for success.
# Source: https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb

if [ -z $1 ]; then echo "Usage: ./$0 RHOST {RPORT}" && exit; else rhost=$1; fi

if [ ! -z $2 ]; then rport=$2; else rport=139; fi

tcpdump -s0 -n -i tap0 src $rhost and port $rport -A -c 7 2>/dev/null | grep -i "samba\|s.a.m" | tr -d '.' | grep -oP 'UnixSamba.*[0-9a-z]' | tr -d '\n' & echo -n "$rhost: " &

echo "exit" | smbclient -L $rhost 1>/dev/null 2>/dev/null

echo "" && sleep .1
