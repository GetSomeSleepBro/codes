# Lab 3 – Building a WAN with Mixed Wired & Wireless LANs (Packet Tracer)

Goal: Interconnect **LAN-1 (wired)** and **LAN-2 (wireless)** across a serial WAN link and verify end-to-end connectivity.

---

## 1. Topology Overview

```
PC-A ─┬─ Switch-0 ─┐       Serial   ┌─ Router-1 ─┬─ Wireless Router ─┬─ PC-C
       |            ├── Router-0 ──┤            │
PC-B ──┘                       10.10.10.0/30    └───────────────────┘
```

• **LAN-1** (left): 192.168.1.0/24  
• **LAN-2** (right): 192.168.2.0/24 (Wi-Fi)  
• **WAN** link: 10.10.10.0/30 (Serial DCE/DTE)

---

## 2. Step-by-Step in Packet Tracer

1. **Place Devices**  
   • 2× **2811 Routers**  
   • 1× **2960 Switch**  
   • 1× **Wireless Router** (Linksys)  
   • 3× **PCs**

2. **Cable Connections**  
   • Switch-0 ↔ PC-A/B: Copper-Straight-Through  
   • Switch-0 ↔ Router-0 (FastEthernet0/0)  
   • Router-0 (Serial0/0/0) ↔ Router-1 (Serial0/0/0) via **Serial DCE/DTE** (remember to set clock rate on DCE side).  
   • Router-1 (FastEthernet0/0) ↔ Wireless Router Internet port.  
   • PCs connect to wireless network later.

3. **IP Addressing**

| Interface | IP | Mask |
|-----------|----|------|
| R0 Fa0/0  | 192.168.1.254 | 255.255.255.0 |
| R0 S0/0/0 | 10.10.10.1    | 255.255.255.252 |
| R1 S0/0/0 | 10.10.10.2    | 255.255.255.252 |
| R1 Fa0/0  | 192.168.2.254 | 255.255.255.0 |
| Wireless Router (LAN) | 192.168.2.1 | 255.255.255.0 |

4. **Routing**  
`Router(config)# ip route 0.0.0.0 0.0.0.0 10.10.10.2` on R0  
`Router(config)# ip route 0.0.0.0 0.0.0.0 10.10.10.1` on R1  
Alternatively enable a dynamic protocol (e.g., RIP v2) as an extension.

5. **Wireless Configuration**  
Wireless Router ▸ GUI tab ▸ Wireless ▸ Basic: SSID = **LAN2-WiFi**. Security tab ▸ WPA2-PSK with a passphrase.

6. **PC Configuration**  
PC-A: 192.168.1.10/24, GW 192.168.1.254  
PC-B: 192.168.1.11/24, GW 192.168.1.254  
PC-C: connect via **PC-Wireless**, IP DHCP or static 192.168.2.10/24, GW 192.168.2.254.

---

## 3. Verification

1. Ping from **PC-A → PC-C**; expect <100 ms.  
2. Open Simulation mode. Add *Simple PDU* from PC-B to PC-C and observe packet path crossing WAN serial then wireless.

---

## 4. Deliverables

• `.pkt` file, ping screenshots, and a short paragraph explaining NAT (if Wireless Router is in NAT mode).

Enjoy experimenting! 
