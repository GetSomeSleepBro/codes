#!/usr/bin/env python3
"""
Routing Algorithm Demonstrator
-----------------------------
Implements both
1. Link-State routing using Dijkstra's shortest path algorithm.
2. Distance Vector routing using the Bellman–Ford algorithm.

Input graph format (plain text file): one edge per line
    node1 node2 cost

Example file (matrix.txt):
    A B 4
    A C 2
    B C 1
    B D 5
    C D 8

Run Dijkstra (link-state) from source A:
    $ python routing.py matrix.txt ls A

Run Distance-Vector (Bellman-Ford) from A:
    $ python routing.py matrix.txt dv A
"""

from __future__ import annotations

import argparse
import math
from collections import defaultdict
from typing import Dict, List, Tuple


Graph = Dict[str, Dict[str, float]]  # adjacency list with costs


def read_graph(path: str) -> Graph:
    graph: Graph = defaultdict(dict)
    with open(path) as f:
        for line in f:
            if not line.strip() or line.startswith('#'):
                continue
            u, v, w = line.split()
            w = float(w)
            graph[u][v] = w
            graph[v][u] = w  # undirected
    return graph


# ------------------------------------------------------------------
# 1. Dijkstra (Link-State)
# ------------------------------------------------------------------


def dijkstra(graph: Graph, src: str) -> Dict[str, float]:
    dist = {node: math.inf for node in graph}
    dist[src] = 0.0
    visited = set()
    while len(visited) < len(graph):
        # node with smallest tentative distance not yet visited
        u = min((n for n in graph if n not in visited), key=lambda n: dist[n], default=None)
        if u is None or dist[u] == math.inf:
            break  # remaining nodes are unreachable
        visited.add(u)
        for v, w in graph[u].items():
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


# ------------------------------------------------------------------
# 2. Bellman-Ford (Distance Vector)
# ------------------------------------------------------------------


def bellman_ford(graph: Graph, src: str) -> Tuple[Dict[str, float], bool]:
    nodes = list(graph)
    dist = {n: math.inf for n in nodes}
    dist[src] = 0.0

    for _ in range(len(nodes) - 1):
        updated = False
        for u in nodes:
            for v, w in graph[u].items():
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
        if not updated:
            break

    # detect negative cycles
    has_neg_cycle = False
    for u in nodes:
        for v, w in graph[u].items():
            if dist[u] + w < dist[v]:
                has_neg_cycle = True
                break
    return dist, has_neg_cycle


# ------------------------------------------------------------------
# Main CLI
# ------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Link-State / Distance-Vector Routing Simulator")
    parser.add_argument("graph", help="Path to graph text file")
    parser.add_argument("algo", choices=["ls", "dv"], help="Routing algorithm: ls (Dijkstra) or dv (Bellman-Ford)")
    parser.add_argument("src", help="Source node")
    args = parser.parse_args()

    g = read_graph(args.graph)
    if args.src not in g:
        print("Source node not in graph.")
        return

    if args.algo == "ls":
        dist = dijkstra(g, args.src)
        print("Shortest paths from", args.src)
        for dst, d in dist.items():
            print(f"  {dst}: {d if d < math.inf else '∞'}")
    else:
        dist, neg = bellman_ford(g, args.src)
        if neg:
            print("Graph contains a negative-weight cycle. Distances below may be invalid.")
        print("Distances from", args.src)
        for dst, d in dist.items():
            print(f"  {dst}: {d if d < math.inf else '∞'}")


if __name__ == "__main__":
    main()
