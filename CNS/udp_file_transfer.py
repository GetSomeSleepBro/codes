#!/usr/bin/env python3
"""
UDP File Transfer (very simple, no reliability)
----------------------------------------------
This script demonstrates file transfer over UDP between two machines.  Because
UDP does not guarantee delivery, ordering, or integrity, the implementation
adds a trivial stop-and-wait reliability layer with sequence numbers and ACKs.

Packet format (all fields unsigned, big-endian):
    uint16 seq   –  sequence number (0/1 toggling)
    uint16 len   –  length of payload bytes that follow (0-1024)
    bytes payload

A zero-length payload marks **End Of Transmission**.

Usage
-----
Server (receiver):
    $ python udp_file_transfer.py server 0.0.0.0 9000 dest_path

Client (sender):
    $ python udp_file_transfer.py client 127.0.0.1 9000 /path/to/file
"""

from __future__ import annotations

import os
import socket
import struct
import sys
import time


PKT_HDR = struct.Struct('!HH')  # seq, length (<=1024)
MAX_PAYLOAD = 1024
ACK_BYTES = b'ACK'
TIMEOUT = 2.0


def recv_packet(sock: socket.socket) -> tuple[int, bytes, tuple[str, int]]:
    data, addr = sock.recvfrom(PKT_HDR.size + MAX_PAYLOAD)
    seq, length = PKT_HDR.unpack(data[:PKT_HDR.size])
    payload = data[PKT_HDR.size:PKT_HDR.size + length]
    return seq, payload, addr


def run_server(host: str, port: int, dest_path: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"[Server] Waiting on {host}:{port} → {dest_path}")

    expected_seq = 0
    with open(dest_path, 'wb') as f:
        while True:
            seq, payload, addr = recv_packet(sock)
            if seq == expected_seq:
                # correct packet
                if payload:
                    f.write(payload)
                expected_seq ^= 1  # toggle 0/1
            # send ACK regardless (resend scenario)
            sock.sendto(ACK_BYTES + bytes([seq]), addr)
            if not payload:
                print("[Server] Transfer complete.")
                break


def run_client(host: str, port: int, file_path: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(TIMEOUT)

    addr = (host, port)
    seq = 0
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(MAX_PAYLOAD)
            if not chunk:
                # send zero-length payload to mark EOF
                packet = PKT_HDR.pack(seq, 0)
                send_with_ack(sock, addr, packet, seq)
                break
            packet = PKT_HDR.pack(seq, len(chunk)) + chunk
            send_with_ack(sock, addr, packet, seq)
            seq ^= 1  # toggle
    print("[Client] File sent successfully.")


def send_with_ack(sock: socket.socket, addr, packet: bytes, seq: int):
    while True:
        sock.sendto(packet, addr)
        try:
            data, _ = sock.recvfrom(16)
            if data.startswith(ACK_BYTES) and data[-1] == seq:
                return
        except socket.timeout:
            print("[Client] Timeout, retransmitting seq", seq)


def main() -> None:
    if len(sys.argv) < 5:
        print("Usage: {} server host port dest_path | client host port file_path".format(sys.argv[0]))
        return
    mode = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
    if mode == 'server':
        dest_path = sys.argv[4]
        run_server(host, port, dest_path)
    else:
        file_path = sys.argv[4]
        run_client(host, port, file_path)


if __name__ == '__main__':
    main()
