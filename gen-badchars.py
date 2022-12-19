#!/usr/bin/python3 
import struct 
import os

output="exploit.txt" # output file
bad_chars = [0x00] # chars excluded from the output

# generating test chars
test_chars = [(struct.pack('B',c) if c not in bad_chars else b'') for c in range(0x00, 0x100)] 

# writing chars to file
open(output,'wb').write(b''.join(test_chars))

# printing file path
absolute_path = os.path.abspath(output)
print("Output saved at: " + absolute_path)

# to check file in Linux: 'xxd exploit.txt'
