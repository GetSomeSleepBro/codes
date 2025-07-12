# Lab 8 – Configuring a 3-Router Network (RIP / OSPF / BGP) in Packet Tracer

This guide shows how to create a triangle-shaped internetwork with three routers and exchange routes via **RIP v2** (also notes for OSPF & BGP).

---

## 1. Topology

```
        10.0.12.0/30           10.0.23.0/30
  (R1)─────────────(R2)────────────────(R3)
          \                       /
           \ 10.0.13.0/30       /
            └───────────────────┘
```

Each router will also have a **Loopback0** representing an internal LAN:

| Router | Loopback0 | Mask |
|--------|-----------|------|
| R1 | 192.168.1.1 | /24 |
| R2 | 192.168.2.1 | /24 |
| R3 | 192.168.3.1 | /24 |

---

## 2. Device Placement & Cabling

* Packet Tracer → place 3× **2911 routers**.  
* Use **Serial0/0/0** & **Serial0/0/1** interfaces to build the triangle (select clock rate on DCE side).  
* Optionally place a **PC** per loopback network for testing (connect via Ethernet).

---

## 3. Base Configuration (R1 shown; repeat for R2 & R3)

```plaintext
enable
conf t
hostname R1
!
interface Serial0/0/0
 ip address 10.0.12.1 255.255.255.252
 clock rate 64000  ! only on DCE side
 no shutdown
!
interface Serial0/0/1
 ip address 10.0.13.1 255.255.255.252
 clock rate 64000
 no shutdown
!
interface Loopback0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
end
wr
```

Repeat with appropriate addresses for R2 & R3.

---

## 4. Enabling the Routing Protocol

### 4.1 RIP v2

```plaintext
router rip
 version 2
 no auto-summary      ! important for discontiguous networks
 network 10.0.0.0
 network 192.168.0.0
```

### 4.2 OSPF (single area 0)

```plaintext
router ospf 1
 network 10.0.0.0 0.0.0.255 area 0
 network 192.168.0.0 0.0.255.255 area 0
```

### 4.3 iBGP (AS 65001)

1. On each router: `router bgp 65001`  
2. Define neighbors using *loopback* addresses:  

```plaintext
neighbor 192.168.2.1 remote-as 65001
neighbor 192.168.3.1 remote-as 65001
```

3. Advertise networks: `network 192.168.X.0 mask 255.255.255.0`

---

## 5. Verification

* `show ip route` – ensure remote loopback networks appear as R/R/IP routes.  
* `ping 192.168.3.1` from R1 → should succeed.  
* In Simulation mode send a **TCP** PDU from PC1 (192.168.1.x) to PC3 (192.168.3.x) and observe multi-hop path.

---

## 6. Deliverables

* `.pkt` file for chosen protocol.  
* `show run` outputs or screenshots demonstrating neighbor relationships.  
* Traceroute result across all three routers.

That’s it – your 3-router network is fully dynamic! 
