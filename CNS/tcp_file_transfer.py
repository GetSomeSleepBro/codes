#!/usr/bin/env python3
"""
TCP File Transfer Utility (client / server)

Server:
    $ python tcp_file_transfer.py server 0.0.0.0 6000 dest_dir

Client:
    $ python tcp_file_transfer.py client 127.0.0.1 6000 path/to/file.bin

Protocol (very simple):
    uint32 filename_length
    bytes  filename (UTF-8)
    uint64 file_size
    bytes  file_content
All integers are unsigned, big-endian.
"""

import os
import socket
import struct
import sys


UINT32 = struct.Struct('!I')
UINT64 = struct.Struct('!Q')


def recv_all(sock: socket.socket, n: int) -> bytes:
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            raise ConnectionError("Unexpected EOF while receiving data")
        data += chunk
    return data


def run_server(host: str, port: int, dest_dir: str):
    os.makedirs(dest_dir, exist_ok=True)
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((host, port))
    srv.listen(1)
    print(f"[Server] Listening on {host}:{port}")
    conn, addr = srv.accept()
    with conn:
        print("[Server] Connection from", addr)
        name_len = UINT32.unpack(recv_all(conn, UINT32.size))[0]
        filename = recv_all(conn, name_len).decode()
        file_size = UINT64.unpack(recv_all(conn, UINT64.size))[0]
        print(f"[Server] Receiving '{filename}' ({file_size} bytes)")
        filepath = os.path.join(dest_dir, os.path.basename(filename))
        with open(filepath, 'wb') as f:
            remaining = file_size
            while remaining:
                chunk = conn.recv(min(4096, remaining))
                if not chunk:
                    raise ConnectionError("Connection lost during file transfer")
                f.write(chunk)
                remaining -= len(chunk)
        print(f"[Server] Saved to {filepath}")
        conn.sendall(b"OK")


def run_client(host: str, port: int, file_path: str):
    with open(file_path, 'rb') as f:
        data = f.read()
    filename = os.path.basename(file_path).encode()
    name_len = len(filename)
    file_size = len(data)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print(f"[Client] Connected to {host}:{port}")
    sock.sendall(UINT32.pack(name_len))
    sock.sendall(filename)
    sock.sendall(UINT64.pack(file_size))
    sock.sendall(data)
    print("[Client] File sent, waiting for confirmation...")
    resp = sock.recv(16)
    print("[Client] Server response:", resp.decode())
    sock.close()


def main():
    if len(sys.argv) < 5:
        print("Usage:")
        print("  Server: {} server host port dest_dir".format(sys.argv[0]))
        print("  Client: {} client host port file_path".format(sys.argv[0]))
        return
    mode = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
    if mode == "server":
        dest_dir = sys.argv[4]
        run_server(host, port, dest_dir)
    else:
        file_path = sys.argv[4]
        run_client(host, port, file_path)


if __name__ == "__main__":
    main()
