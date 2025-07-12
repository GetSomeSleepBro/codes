# Wireshark Master Guide & Pro Tips

*Version: 2023-09 – written for Wireshark 4.x*

---

## 1. Interface Selection

• **List all interfaces** – Home screen lists NICs with live traffic counters.  
• For USB tethering use *“usbX”* or *“enp0s20f0u2”*.  
• Right-click → **Manage Interfaces** to rename & mark favourites.

---

## 2. Capture Filters Cheat-Sheet (BPF syntax)

| Task | Filter |
|------|--------|
| Only HTTP | `tcp port 80` |
| Capture one host | `host 192.168.1.5` |
| Range of hosts | `net 10.0.0.0/24` |
| Exclude broadcast/multicast | `not ether dst ff:ff:ff:ff:ff:ff and not multicast` |
| VoIP (SIP & RTP) | `port 5060 or udp portrange 16384-32767` |

Apply via **Capture Options ▸ Capture Filter**.

---

## 3. Display Filters Cheat-Sheet (Wireshark syntax)

| Purpose | Filter |
|---------|--------|
| Show only DNS | `dns` |
| TCP SYN packets | `tcp.flags.syn == 1 and tcp.flags.ack == 0` |
| HTTP POSTs | `http.request.method == "POST"` |
| TLS 1.3 Handshake | `tls.handshake.type == 1` (ClientHello) |
| Packet size > 1000 bytes | `frame.len > 1000` |

Press **Ctrl+L** to focus the filter bar, **Ctrl+Space** for autocompletion.

---

## 4. Colouring Rules

1. Menu ▸ *View ▸ Coloring Rules*.  
2. Useful additions:
   * Green background – `tcp.flags.syn == 1 and tcp.flags.ack == 0` (SYN).  
   * Orange – `tcp.analysis.retransmission` (retransmissions).  
3. Hit **Save As Default** to persist.

---

## 5. Profiles & Configuration Portability

• Profiles—including colour rules, column layouts, captured preferences—are stored in `~/.config/wireshark/profiles/<ProfileName>` (Linux) or `%APPDATA%\Wireshark\profiles`.  
• Export the folder to replicate your tuning on lab PCs.

---

## 6. Columns Every Analyst Adds

1. **Delta Time Displayed** – inter-packet gap.  
2. **Stream index** – useful for multi-flow tracing (`tcp.stream`).  
3. **Packet size** – `frame.len`.  
Right-click any column header ▸ *Column Preferences*.

---

## 7. Follow & Export

• **Follow Stream** – supports TCP, UDP, HTTP, TLS, ICMP, …  
• Export as *Raw* or *Hex Dump*.  
• For binary file reconstruction use *Follow TCP Stream* ➝ Save As *raw*.

---

## 8. Expert Infos & IO Graphs

* Analyze ▸ **Expert Information** – highlights warnings (checksum errors, retransmissions).  
* Statistics ▸ **I/O Graphs** – plot throughput: add Graph → Filter = `tcp`, Y-field = Bytes, Tick Interval = 0.1 s.

---

## 9. Pro Tips

1. **Name Resolution Hot-Key** – `Ctrl+H` toggles DNS & MAC name resolution on the fly.  
2. **‘!tcp.analysis.initial_rtt’** Trick – quickly list flows missing handshake.  
3. **Decode As…** – right-click packet ▸ decode non-standard ports (e.g., treat 8443 as TLS).  
4. **Time Shift** – Edit ▸ Time Shift to align captures from different devices.  
5. **Packet Comments** – annotate frames for reports (Packet ▸ Packet Comment).  
6. **Alt + ↑/↓** – move up/down inside the packet details tree.  
7. **Wireless monitor mode** – turn on *IEEE 802.11* radio headers on laptops with compatible cards.  
8. **CPU Friendly Capture** – enable *Synchronous scroll* OFF and disable colourisation during heavy live captures.

---

## 10. Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Start capture | `Ctrl+E` |
| Stop capture | `Ctrl+E` again |
| Restart capture | `Ctrl+R` |
| Apply display filter | `Enter` |
| Clear filter | `Ctrl+Shift+C` |
| Find packet | `Ctrl+F` |
| Mark packet | `Ctrl+M` |
| Next marked | `Ctrl+Shift+N` |

---

## 11. Further Learning Resources

* Official docs: https://www.wireshark.org/docs/  
* Laura Chappell’s “Wireshark Network Analysis” book.  
* Hack-Tricks Wireshark page for capture-the-flag style use-cases.

Happy sniffing! 
