#!/usr/bin/env python3
"""
DNS Lookup Utility
------------------
Provide an IPv4 address to obtain its PTR record (reverse lookup) or provide a
hostname to resolve its A record.

Examples
    $ python dns_lookup.py google.com
    $ python dns_lookup.py 8.8.8.8
"""

import socket
import sys


def lookup(query: str):
    # Is it an IP?
    try:
        socket.inet_aton(query)
        is_ip = True
    except OSError:
        is_ip = False

    try:
        if is_ip:
            host, _, _ = socket.gethostbyaddr(query)
            print(f"{query} → {host}")
        else:
            ip = socket.gethostbyname(query)
            print(f"{query} → {ip}")
    except socket.herror as e:
        print("Lookup failed:", e)


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <hostname>|<ip>".format(sys.argv[0]))
        return
    lookup(sys.argv[1])


if __name__ == "__main__":
    main()
