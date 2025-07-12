# Lab 14 – Comparing HTTP, HTTPS & FTP Performance in Packet Tracer

This qualitative study shows how much overhead encryption introduces by timing file transfers and measuring throughput.

---

## 1. Lab Topology

```
PC-Client ─── Switch ─── Server-PT (HTTP/HTTPS/FTP)
```

1. Place **Server-PT** and install three services: **HTTP**, **HTTPS**, **FTP** (Config tab ▸ Services).  
2. Connect a **PC** via Copper-Straight-Through (same VLAN).  
3. Use network 10.0.0.0/24.

---

## 2. Preparing Test File

On Server-PT ▸ Services ▸ FTP ▸ Add `test.bin` of 5 MB.

---

## 3. Measuring Transfer Time

1. Switch Packet Tracer to **Simulation** mode.  
2. On the PC, open Web Browser:
   * HTTP: `http://10.0.0.1/test.bin`  
   * HTTPS: `https://10.0.0.1/test.bin` (enable HTTPS service).

3. For FTP open the **FTP Client** tab: `ftp 10.0.0.1`, get `test.bin`.

4. Observe timestamps of first and last packet in Simulation pane; difference ≈ transfer time.

5. Calculate throughput = `file_size / time`.  Repeat three times per protocol.

---

## 4. Expected Observations

| Protocol | Extra Handshake | Avg RTTs | Comments |
|----------|-----------------|----------|----------|
| HTTP     | None            | 1        | Fastest – plain TCP 3-way handshake + GET |
| HTTPS    | TLS Handshake (~2 RTT) | 3 | Takes longer before data flows; encryption overhead |
| FTP      | Control + Data connections | 2 | Active vs passive affects latency |

Plot a bar chart of throughput; HTTPS usually ~5-10 % slower.

---

## 5. Deliverables

• Screenshot of Simulation timeline for each protocol.  
• Table summarising timing and throughput.  
• 2–3 sentences interpreting results.

---

## 6. Extra Credit

1. Introduce 50 ms latency (`Config ▸ Interface ▸ Delay`) and repeat tests.  
2. Use Wireshark to capture TLS handshake and identify **ClientHello**/**ServerHello**.

Good luck analysing! 
