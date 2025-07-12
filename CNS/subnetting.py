#!/usr/bin/env python3
"""
Subnetting Helper
-----------------
This small CLI assists with basic IPv4 subnetting calculations.

Supported operations
1. Given a network in CIDR notation and *k* required sub-nets, list all resulting
   sub-networks of equal size.
   Example:
       $ python subnetting.py split 192.168.1.0/24 4

2. Given a network in CIDR notation and a comma-separated list with the number
   of hosts each sub-network must support, produce Variable Length Subnet Mask
   (VLSM) allocation.
   Example:
       $ python subnetting.py vlsm 10.0.0.0/24 100,50,25,25

3. Given an IP address & netmask, print the network address, broadcast address
   and host count.
   Example:
       $ python subnetting.py info 10.1.2.3 255.255.255.0
"""

import argparse
import ipaddress
import math
from typing import List


def split_equal(network: str, k: int):
    net = ipaddress.IPv4Network(network, strict=False)
    new_prefix = net.prefixlen + math.ceil(math.log2(k))
    if new_prefix > 30:
        raise ValueError("Too many subnets requested; prefix would be /{}".format(new_prefix))
    subnets = list(net.subnets(new_prefix=new_prefix))[:k]
    print(f"{network} split into {k} subnets (/{new_prefix}):")
    for s in subnets:
        print(f"  {s}  hosts={s.num_addresses - 2}")


def vlsm(network: str, host_reqs: List[int]):
    net = ipaddress.IPv4Network(network, strict=False)
    # sort hosts descending to minimise waste
    host_reqs = sorted(host_reqs, reverse=True)
    current_base = int(net.network_address)
    last = int(net.broadcast_address)

    print("VLSM allocation inside {}:".format(net.with_prefixlen))
    for hosts in host_reqs:
        needed = hosts + 2  # network + broadcast
        bits = math.ceil(math.log2(needed))
        subnet_size = 2 ** bits
        prefix = 32 - bits
        if current_base + subnet_size - 1 > last:
            raise RuntimeError("Insufficient address space for all requested subnets.")
        subnet = ipaddress.IPv4Network((current_base, prefix))
        print(f"  {subnet}  hosts_supported={subnet.num_addresses - 2}  (requested {hosts})")
        current_base += subnet_size


def info(ip: str, mask: str):
    network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)
    print("Network:", network.network_address)
    print("Broadcast:", network.broadcast_address)
    print("Netmask:", network.netmask)
    print("Wildcard mask:", ipaddress.IPv4Address(~int(network.netmask) & 0xFFFFFFFF))
    print("Hosts per subnet:", network.num_addresses - 2)


def main():
    parser = argparse.ArgumentParser(description="IPv4 Subnetting Helper")
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    split_p = subparsers.add_parser("split", help="Split a network into equal-sized subnets")
    split_p.add_argument("network", help="Base network in CIDR (e.g. 192.168.0.0/24)")
    split_p.add_argument("k", type=int, help="Desired number of subnets (power-of-two rounded up)")

    vlsm_p = subparsers.add_parser("vlsm", help="Variable Length Subnet Mask allocation")
    vlsm_p.add_argument("network", help="Base network in CIDR")
    vlsm_p.add_argument("hosts", help="Comma-separated host counts per subnet (e.g. 100,50,20)")

    info_p = subparsers.add_parser("info", help="Show network information for IP & mask")
    info_p.add_argument("ip", help="IP address")
    info_p.add_argument("mask", help="Subnet mask (dotted or /prefix)")

    args = parser.parse_args()

    if args.cmd == "split":
        split_equal(args.network, args.k)
    elif args.cmd == "vlsm":
        host_reqs = [int(h) for h in args.hosts.split(',') if h]
        vlsm(args.network, host_reqs)
    elif args.cmd == "info":
        info(args.ip, args.mask)


if __name__ == "__main__":
    main()
