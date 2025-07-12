#!/usr/bin/env python3
"""
Sliding Window Protocol Simulator (Go-Back-N & Selective Repeat)
---------------------------------------------------------------
This self-contained simulation exchanges data between a *Sender* and a *Receiver*
through an *UnreliableChannel* that randomly drops DATA and ACK packets with a
configurable probability.  It is meant for classroom / lab demonstration – it
is **not** a production-grade network stack.

Key Simplifications
• Time is discrete. At every *tick* the following happens in order:
    1. Sender transmits as many DATA packets as the window allows.
    2. The channel tries to deliver all in-flight DATA packets to the receiver.
    3. The receiver processes each DATA packet (possibly buffering it) and sends
       the appropriate ACK(s).
    4. The channel tries to deliver all in-flight ACKs to the sender.
    5. Timers of all outstanding DATA packets are decremented; those that reach
       zero cause a retransmission (timeout = 5 ticks).
• Each DATA packet carries exactly one character of the user-supplied message.
• There is a single end-to-end direction (sender ➜ receiver).

Usage
-----
    python sliding_window.py "HELLO WORLD"        # Go-Back-N, window=4, loss=0.1
    python sliding_window.py "DATA" --protocol sr --window 3 --loss 0.3

While the simulation is running it prints an easy-to-read trace.
"""

from __future__ import annotations

import argparse
import random
from collections import deque
from typing import Deque, Dict, List, Tuple


Packet = Tuple[int, str]  # (sequence_number, payload)


class UnreliableChannel:
    """Bi-directional channel that randomly drops packets."""

    def __init__(self, loss_prob: float):
        self.loss_prob = loss_prob
        self.data_queue: Deque[Packet] = deque()  # sender ➜ receiver
        self.ack_queue: Deque[Packet] = deque()   # receiver ➜ sender

    # Enqueue helpers -----------------------------------------------------
    def send_data(self, pkt: Packet):
        self.data_queue.append(pkt)

    def send_ack(self, pkt: Packet):
        self.ack_queue.append(pkt)

    # Delivery helpers ----------------------------------------------------
    def _deliver(self, q: Deque[Packet], direction: str) -> List[Packet]:
        delivered: List[Packet] = []
        while q:
            pkt = q.popleft()
            if random.random() < self.loss_prob:
                print(f"[CHANNEL]   {direction.upper()} packet LOST  seq={pkt[0]}")
            else:
                delivered.append(pkt)
        return delivered

    def deliver_data(self) -> List[Packet]:
        return self._deliver(self.data_queue, "data")

    def deliver_ack(self) -> List[Packet]:
        return self._deliver(self.ack_queue, "ack")


class Sender:
    def __init__(self, message: str, wnd: int, proto: str, ch: UnreliableChannel):
        self.msg = message
        self.window = wnd
        self.protocol = proto  # "gbn" or "sr"
        self.ch = ch

        # state
        self.next_seq = 0  # smallest unused sequence number
        self.base = 0      # oldest unacknowledged sequence number (GBN)
        self.timers: Dict[int, int] = {}  # seq -> ticks remaining
        self.unacked: Dict[int, str] = {}  # seq -> payload

    # Phase 1 – send --------------------------------------------------------------------
    def send_packets(self):
        while len(self.unacked) < self.window and self.next_seq < len(self.msg):
            payload = self.msg[self.next_seq]
            pkt: Packet = (self.next_seq, payload)
            print(f"[SENDER]    SEND  seq={pkt[0]} data='{pkt[1]}'")
            self.ch.send_data(pkt)
            self.unacked[pkt[0]] = pkt[1]
            self.timers[pkt[0]] = 5  # timeout value (ticks)
            self.next_seq += 1

    # Phase 4 – process ACKs -------------------------------------------------------------
    def handle_acks(self, acks: List[Packet]):
        for seq, _ in acks:
            if self.protocol == "gbn":
                # cumulative ACK – acknowledge everything ≤ seq
                if seq >= self.base:
                    for s in range(self.base, seq + 1):
                        self.unacked.pop(s, None)
                        self.timers.pop(s, None)
                    self.base = seq + 1
                    print(f"[SENDER]    ACK  cumulative up to {seq}")
            else:  # SR – individual ACKs
                if seq in self.unacked:
                    self.unacked.pop(seq)
                    self.timers.pop(seq, None)
                    print(f"[SENDER]    ACK  seq={seq}")

    # Phase 5 – timers ------------------------------------------------------------------
    def tick_timers(self):
        for seq in list(self.timers):
            self.timers[seq] -= 1
            if self.timers[seq] == 0:
                # timeout ➜ retransmit (GBN: everything ≥ seq, SR: only seq)
                print(f"[SENDER]    TIMEOUT seq={seq}")
                if self.protocol == "gbn":
                    for s in sorted(self.unacked):
                        if s >= seq:
                            pkt: Packet = (s, self.unacked[s])
                            print(f"[SENDER]    RE-SEND seq={s} data='{pkt[1]}' (GBN)")
                            self.ch.send_data(pkt)
                            self.timers[s] = 5
                    break  # Only one timeout needed to trigger whole window
                else:
                    pkt = (seq, self.unacked[seq])
                    print(f"[SENDER]    RE-SEND seq={seq} data='{pkt[1]}' (SR)")
                    self.ch.send_data(pkt)
                    self.timers[seq] = 5

    # Termination check -----------------------------------------------------------------
    def done(self) -> bool:
        return self.base >= len(self.msg)


class Receiver:
    def __init__(self, wnd: int, proto: str, ch: UnreliableChannel):
        self.window = wnd
        self.protocol = proto
        self.ch = ch

        self.expected = 0          # next in-order sequence number (GBN + SR)
        self.buffer: Dict[int, str] = {}  # out-of-order packets (SR only)
        self.output: List[str] = []

    # Phase 3 – process DATA packets -----------------------------------------------------
    def receive(self, pkts: List[Packet]):
        for seq, payload in pkts:
            if self.protocol == "gbn":
                if seq == self.expected:
                    self.output.append(payload)
                    self.expected += 1
                # Whether in-order or not, send cumulative ACK for last delivered
                ack_pkt: Packet = (self.expected - 1, "")
                self.ch.send_ack(ack_pkt)
                print(f"[RECEIVER]  RCV  seq={seq} → ACK {ack_pkt[0]}")
            else:  # SR
                if self.expected <= seq < self.expected + self.window:
                    self.ch.send_ack((seq, ""))
                    print(f"[RECEIVER]  RCV  seq={seq} → ACK {seq}")
                    if seq == self.expected:
                        # deliver in-order and slide window past contiguous block
                        self.output.append(payload)
                        self.expected += 1
                        while self.expected in self.buffer:
                            self.output.append(self.buffer.pop(self.expected))
                            self.expected += 1
                    else:
                        # buffer out-of-order
                        self.buffer[seq] = payload


def simulate(message: str, protocol: str, window: int, loss_prob: float):
    random.seed(42)
    ch = UnreliableChannel(loss_prob)
    snd = Sender(message, window, protocol, ch)
    rcv = Receiver(window, protocol, ch)

    tick = 0
    while not snd.done():
        print(f"\n--- TICK {tick} ---")
        snd.send_packets()               # Phase 1
        delivered_data = ch.deliver_data()  # Phase 2
        rcv.receive(delivered_data)         # Phase 3 (may enqueue ACKs)
        delivered_acks = ch.deliver_ack()   # Phase 4
        snd.handle_acks(delivered_acks)
        snd.tick_timers()                # Phase 5
        tick += 1
        if tick > 1000:  # safety valve
            print("Simulation aborted (too many ticks).")
            break

    print("\n=== RECEIVER OUTPUT ===")
    print(''.join(rcv.output))


def main() -> None:
    parser = argparse.ArgumentParser(description="Go-Back-N / Selective Repeat Simulator")
    parser.add_argument("message", help="Message to send")
    parser.add_argument("--protocol", choices=["gbn", "sr"], default="gbn", help="Protocol to simulate")
    parser.add_argument("--window", type=int, default=4, help="Sender/receiver window size")
    parser.add_argument("--loss", type=float, default=0.1, help="Packet loss probability (0-1)")
    args = parser.parse_args()

    simulate(args.message, args.protocol, args.window, args.loss)


if __name__ == "__main__":
    main()
