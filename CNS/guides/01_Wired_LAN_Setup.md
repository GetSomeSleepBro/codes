# Lab 1 – Setting-Up a Wired LAN with a Layer-2 Switch

This guide walks you through building a basic **Ethernet LAN** with a layer-2 switch and two (or more) PCs.  It covers cable preparation, IP addressing, connectivity testing, and viewing live traffic with Wireshark.

---

## 1. Hardware / Materials

1. **Layer-2 switch** – unmanaged is fine (e.g., Cisco Catalyst 2960, TP-Link TL-SG108).  
2. **PCs / Laptops** – at least two, each with a NIC.  
3. **RJ-45 connectors** and **Cat-5e / Cat-6 UTP** cable.  
4. **Crimping tool** & **wire-cutter / stripper**.  
5. **Network cable tester (line-tester)** – verifies pinout continuity.

> If you do not have physical equipment, you can reproduce the topology in **Cisco Packet Tracer** – simply drag-and-drop a 2960 switch and two PCs and connect with copper-straight-through cables.

---

## 2. Cable Preparation (TIA/EIA-568B pinout)

| Pin | Wire Colour |
|-----|-------------|
| 1   | White/Orange|
| 2   | Orange      |
| 3   | White/Green |
| 4   | Blue        |
| 5   | White/Blue  |
| 6   | Green       |
| 7   | White/Brown |
| 8   | Brown       |

1. **Strip** ~2 cm of the outer sheath.  
2. Untwist pairs, align wires per the table, and trim to equal length.  
3. Insert firmly into the RJ-45 plug (tab facing down, pin 1 left).  
4. **Crimp** – ensure the strain relief bites the jacket.  
5. Repeat for the other end (straight-through cable).

### 2.1 Testing the Cable

1. Connect both ends to the line-tester.  
2. LEDs 1–8 should illuminate sequentially **1-2-3-4-5-6-7-8**.  
3. Any cross-over / open / short will show a mismatch; re-crimp as needed.

---

## 3. Physical Topology

```
┌────────┐    CAT5e     ┌────────┐     CAT5e    ┌────────┐
│  PC-1  │─────────────│ Switch │──────────────│  PC-2  │
└────────┘             └────────┘              └────────┘
```

Plug the freshly crimped cables into any **access-layer** ports (e.g., FastEthernet0/1 and 0/2).

---

## 4. IP Addressing

| Device | Interface | IP Address   | Subnet Mask | Default GW |
|--------|-----------|--------------|-------------|------------|
| PC-1   | eth0      | 192.168.1.10 | 255.255.255.0 | — |
| PC-2   | eth0      | 192.168.1.20 | 255.255.255.0 | — |

On Windows 10/11:

```powershell
Settings ▸ Network & Internet ▸ Change adapter options ▸ Ethernet ▸ Properties ▸ IPv4 ▸ “Use the following”.
```

On Linux:

```bash
sudo ip addr add 192.168.1.10/24 dev eth0    # PC-1
sudo ip addr add 192.168.1.20/24 dev eth0    # PC-2
```

---

## 5. Connectivity Tests

1. On **PC-1** open a terminal / cmd and run:

   ```bash
   ping 192.168.1.20
   ```

2. You should see <1 ms replies.  Any “Request timed out” indicates cabling or IP issues.

3. Optionally run a continual ping (`ping -t` on Windows / `ping 192.168.1.20` on Linux) while you move cables to stress-test.

---

## 6. Capture the Ping with Wireshark

1. Install Wireshark (https://www.wireshark.org).  
2. Start Wireshark on **PC-1** and choose the active Ethernet interface.  
3. In the **Display Filter** field, enter `icmp` to show only echo requests/replies.  
4. Begin a ping; you will immediately see `Echo (ping) request` / `Echo (ping) reply` frames.

5. Right-click any packet ▸ **Follow ▸ ICMP Stream** for a consolidated view.

> **Tip:** Save the capture as `wired_lan_ping.pcapng` for your lab record.

---

## 7. Cleanup & Deliverables

• Screenshot of the physical setup (switch + cables).  
• Screenshot of successful ping and Wireshark capture.  
• Copy of the `.pcapng` file.

---

## Troubleshooting Checklist

| Symptom | Possible Cause | Fix |
|---------|----------------|-----|
| No LINK light | Bad crimp / wrong pinout | Re-crimp both ends, verify with tester |
| "Destination host unreachable" | Wrong IP/subnet | Re-configure IPv4 settings |
| Unstable ping (drops) | Loose connector or faulty port | Change port / patch-cord |

Happy networking! 
