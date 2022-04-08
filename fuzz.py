#!/bin/python3

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
#     python script using an incremental payload to fuzz a remote target 
#       over TCP sending an unformatted sequence of bytes (e.g., 'AABBCC..')
# 	
#     Usage:
#       python3 fuzz.py <target-IPv4> <target-port>
#     Example of usage:
#       python3 fuzz.py 192.168.0.1 9999
#
#     This script is inspired from the Udemy course "Practical Ethical 
#     Hacking - The Complete Course" taught by Heath Adams.
#   % ====================================================================== %
#
#   TODO: add the possibility to provide as a parameter an HTTP request file
#          (e.g., downloaded from BURP) and the position in this request 
#           where to insert the payload to fuzz.
#

import sys
import socket
import time
import random
from datetime import datetime
from string import ascii_uppercase, ascii_lowercase, digits
from itertools import chain

########################## TO CUSTOMIZE ##########################
step = 100              # increase in number of characters per loop
preString = ""          # string to prepend to the buffer
postString = ""         # string to append to the buffer
#################################################################


def validate_IpPort(iIP, iPort):
    validate = 0
    
    try:
        # Translate hostname to target IPv4
        tIP = socket.gethostbyname(iIP)     
    except Exception:
        print("[X] Invalid IP")
        validate = 1
    try:
        tPort = int(iPort)  
    except ValueError:
        print("[X] Invalid Port")
        validate = 1
    
    if validate == 1:
        sys.exit()
        
    return tIP, tPort
     

if __name__ == '__main__':
    
    # Check number of parameters
    if len(sys.argv) != 3:
        print("[X] Wrong number of arguments.")
        print("Usage: python3 {} <target-IPv4> <target-port>".format(sys.argv[0]))
        sys.exit(1)
        
    # Define the target
    IP, port = validate_IpPort(sys.argv[1], sys.argv[2])

    # Print banner
    print("-"*50)
    print("[*] Target: {} : {}".format(IP,port))
    sTime = datetime.now()
    print("[*] Time started: {}".format(sTime))
    print("-"*50)
    
    
    print("[*] Starting fuzzing")
    connected = 0
    buffer = ""
    while True:
        source_chars = chain(ascii_uppercase, ascii_lowercase, digits) # set iterator
        for c in source_chars:
            try:
                # Connect to the target
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((IP,port))
                connected = 1 
                
                # generate payload
                buffer = buffer + c * step
                payload = preString + buffer + postString
                
                # Send payload
                print("[*] Sending buffer ({} bytes)".format(len(buffer)))
                s.sendall(payload.encode())
                #print(payload)
                s.close()
                
                # pause
                time.sleep(0.5)
                
            except Exception as e:
                #print("[X] Error: {}".format(e.message))
                if connected == 0:
                    print("[X] Connection failed.")
                else:
                    print("[+] Target crashed (buffer: {} bytes)".format(len(buffer)))
                sys.exit()
