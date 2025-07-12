#!/usr/bin/env python3
"""
Simple TCP "Hello" program.

Run server:
    $ python tcp_hello.py server 0.0.0.0 5000

Run client:
    $ python tcp_hello.py client 127.0.0.1 5000
"""

import socket
import sys


def run_server(host: str, port: int):
    srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv_sock.bind((host, port))
    srv_sock.listen(1)
    print(f"[Server] Listening on {host}:{port} ...")
    conn, addr = srv_sock.accept()
    with conn:
        print("[Server] Connected by", addr)
        data = conn.recv(1024)
        print("[Server] Received:", data.decode())
        conn.sendall(b"Hello from server!")
    srv_sock.close()


def run_client(host: str, port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(b"Hello from client!")
    data = sock.recv(1024)
    print("[Client] Received:", data.decode())
    sock.close()


def main():
    if len(sys.argv) < 4:
        print("Usage: {} server|client host port".format(sys.argv[0]))
        return
    mode, host, port = sys.argv[1], sys.argv[2], int(sys.argv[3])
    if mode == "server":
        run_server(host, port)
    else:
        run_client(host, port)


if __name__ == "__main__":
    main()
