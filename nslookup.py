#!/usr/bin/env python
# Author: Prometheus - at - rb-cc.ie
# dnsl-list.py - Bulk DNS lookups from text file.
import socket
# Update file path to reflect your source file.
file = "servers.txt"
# Function to verify IP address format.
def isIP(address):
    try:
        socket.inet_aton(address)
        ip = True
    except socket.error:
        ip = False
    return ip
# Open the file to read, pass to variable then close.
f = open(file, 'r')
lines = f.readlines()
f.close()
# Lookup each hostname in turn.
for i in lines:
    host = i.strip()
    try:
        ipaddr = socket.gethostbyname(host)
        if isIP(ipaddr):
            print("%s - %s" % (host, ipaddr))
    except: # Handle error when lookup fails.
            print("%s - No IP address found." % (host))
            pass
