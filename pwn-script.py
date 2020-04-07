#!/usr/bin/python2.7

#
# Simple script that uses pwntool to interact with a local or remote binary
# and extract the return address offset in case of segmentation fault
#
# TODO to further expand using ROPchain for actually exploiting the segmentation fault

from pwn import *
import sys


def exploit(conn):
    # Generate the segmentation fault
    conn.sendline(cyclic(2048))
    conn.wait()
    conn.close()

    # Analyse the coredump to get the return address
    core = Coredump("./core")
    offset = cyclic_find(core.fault_addr)
    log.info("offset found: {}".format(offset))

    #conn.send(b'USER anonymous\r\n')
    #conn.sendline("I am an example")
    #conn.recvline()
    #conn.recvuntil(b' ', drop=True)
    return

if __name__ == '__main__':
    context.log_level =  "DEBUG"

    if len (sys.argv) < 2: #or len(sys.argv) > 4:
        print("Usage: {} [BINARY] [HOST] [PORT]".format(sys.argv[0]))
        exit()

    if len (sys.argv) > 2:
        host = sys.argv[2]
        port = sys.argv[3]
        conn =  remote(host, port)
    else:
        context.binary = sys.argv[1] 
        conn = process(context.binary.path)

    exploit(conn)

