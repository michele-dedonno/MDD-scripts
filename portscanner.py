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
#
#       Basic single-thread port scanner.
#      
#       Usage:
#           python3 portscanner.py <IPv4>
#       Example of usage:
#            python3 portscanner.py 192.168.0.1
#   % ====================================================================== %


import sys
import socket
from datetime import datetime

# Define the target
if len(sys.argv) != 2:
    print("Wrong number of arguments.")
    print("Usage: python3 portscanner.py <IPv4>")
    sys.exit(1)

# Translate hostname to IPv4
targetIP = socket.gethostbyname(sys.argv[1])

# Print banner
print("-"*50)
print("Scanning target: "+targetIP)
print("Time started: "+str(datetime.now()))
print("-"*50)

# Start scanning
try:
        print("Ports open:")
        for port in range(1,65536):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
            socket.setdefaulttimeout(1) # timeout for connection try
            result = s.connect_ex((targetIP,port)) # return an error indicator
            if result == 0:
                print("\t"+str(port))
            s.close()
            # if result == 1: error
except KeyboardInterrupt:
    # Clean exit in case of CTRL+C or other keyboard interrupts
    print("Exiting program.")
    sys.exit()
except socket.gaierror:
    print("Error: Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Error: Could not connect to the server.")
    sys.exit()
