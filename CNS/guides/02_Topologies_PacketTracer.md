# Lab 2 – Visualising Network Topologies & Transmission Media in Cisco Packet Tracer

Objective: Use **Cisco Packet Tracer** to draw and simulate common network topologies (Bus, Ring, Star, Mesh, Hybrid) and compare copper, fibre-optic and wireless media characteristics.

---

## 1. Preparation

1. Install Packet Tracer 8.x (NetAcad).  
2. Familiarise yourself with the workspace – left pane ⇒ devices, bottom ⇒ physical/media options.

---

## 2. Drawing the Topologies

### 2.1 Star Topology (most typical)

1. Drag one **2960 switch** into the canvas.  
2. Add **4× PCs** around it.  
3. Connect each PC with **Copper-Straight-Through** cables to the switch ports FastEthernet0/1-0/4.  
4. Assign IPs 10.0.0.1/24 – 10.0.0.4/24 and test ping.

### 2.2 Bus Topology (legacy)

1. Choose **HUB-PT** as the shared medium.  
2. Attach PCs via **Copper-Straight-Through**.  Hub replicates frames to all.

### 2.3 Ring Topology (token-ring flavour)

Packet Tracer lacks a native token-ring device; simulate with switches: connect each switch *port-to-port* in a closed loop and attach PCs to each switch.  Use **STP** to avoid loops.

### 2.4 Mesh / Partial Mesh

1. Place **4 routers**.  
2. Interconnect every router pair with a **Serial DCE/DTE** link (or GigabitEthernet).  
3. Observe redundancy and multiple paths.

### 2.5 Hybrid

Combine star (access) + mesh (core) by adding switches under each router.

> Save each topology in a separate `.pkt` file for submission.

---

## 3. Comparing Transmission Media

| Medium | Icon | Max Speed | Typical Distance | Notes |
|--------|------|----------|------------------|-------|
| Copper (UTP) | `Copper-Straight-Through` | 1 Gbps (Cat-5e) | 100 m | Susceptible to EMI |
| Fibre (SM/MM) | `Fiber` | 40 Gbps+ | 10 km+ | Immune to EMI, costly |
| Wireless | `Wireless Router` + `PC-Wireless` | 1.3 Gbps (802.11ac) | 30 m indoor | Shared medium, interference |

### 3.1 Demonstration Steps

1. Star topology: duplicate PCs with three links – UTP, Fibre and Wireless.  
2. Use **Add Simple PDU** tool to send a packet; observe propagation delay in the Simulation tab (slower for wireless due to CSMA/CA overhead).  
3. Change link speed/duplex (right-click interface ▸ Config) and note impact.

---

## 4. Deliverables

• `.pkt` files for each topology.  
• Screenshot table comparing latency (from Simulation view).  
• A brief paragraph on pros/cons of each media & topology.

Happy tracing! 
