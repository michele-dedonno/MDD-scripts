#!/bin/python3
# Basic single-thread port scanner

import sys
import socket
from datetime import datetime

# Usage:
# python3 portscanner.py <IPv4>

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