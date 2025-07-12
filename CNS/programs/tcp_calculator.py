#!/usr/bin/env python3
"""
TCP Calculator – evaluate arithmetic expression remotely.

Server side:
    $ python tcp_calculator.py server 0.0.0.0 7000

Client side:
    $ python tcp_calculator.py client 127.0.0.1 7000 "(3+4)*5"
"""

import ast
import operator
import socket
import sys


# Allowed operators mapping for safe evaluation
OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}


def safe_eval(expr: str):
    """Safely evaluate arithmetic expression using AST parsing."""
    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        if isinstance(node, ast.UnaryOp):
            return OPS[type(node.op)](_eval(node.operand))
        if isinstance(node, ast.BinOp):
            return OPS[type(node.op)](_eval(node.left), _eval(node.right))
        raise ValueError("Unsupported expression")

    parsed = ast.parse(expr, mode='eval').body
    return _eval(parsed)


def run_server(host: str, port: int):
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((host, port))
    srv.listen(1)
    print(f"[Server] Listening on {host}:{port}")
    conn, addr = srv.accept()
    with conn:
        print("[Server] Connection from", addr)
        expr = conn.recv(1024).decode().strip()
        print("[Server] Received expression:", expr)
        try:
            result = str(safe_eval(expr))
        except Exception as e:
            result = f"Error: {e}"
        conn.sendall(result.encode())


def run_client(host: str, port: int, expr: str):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(expr.encode())
    result = sock.recv(1024).decode()
    print("Result:", result)
    sock.close()


def main():
    if len(sys.argv) < 4:
        print("Usage: {} server host port | client host port expression".format(sys.argv[0]))
        return
    mode = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
    if mode == "server":
        run_server(host, port)
    else:
        expr = ' '.join(sys.argv[4:])
        run_client(host, port, expr)


if __name__ == "__main__":
    main()
