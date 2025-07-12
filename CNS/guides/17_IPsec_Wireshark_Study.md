# Lab 17 – Analysing IPsec (ESP & AH) with Wireshark

IPsec secures IP packets in transit via **ESP (Encapsulating Security Payload)** and/or **AH (Authentication Header)**.  This lab captures and inspects IPsec traffic between two VPN gateways.

---

## 1. Test Environment

1. Two Linux VMs (Gateway-A 10.1.1.1, Gateway-B 10.2.2.1).  
2. StrongSwan or Libreswan to form an IPsec tunnel (transport or tunnel mode).  
3. Alternatively, emulate in GNS3 / Packet Tracer 8.2 (supports basic IPsec in routers).

### Example StrongSwan configuration (tunnel mode)

```ini
conn site-to-site
    left=10.1.1.1
    leftsubnet=192.168.1.0/24
    right=10.2.2.1
    rightsubnet=192.168.2.0/24
    keyexchange=ikev2
    authby=psk
    ike=aes256-sha256-modp1024!
    esp=aes256-sha256!
    auto=start
```

---

## 2. Capturing the Traffic

1. On Gateway-A run:

   ```bash
   sudo tcpdump -i eth0 -w ipsec_traffic.pcap esp or ah or udp port 500 or udp port 4500
   ```

2. Initiate traffic from LAN-A (192.168.1.x) to LAN-B (192.168.2.x), e.g., ping.

3. Stop capture after few packets.

---

## 3. Wireshark Analysis

1. Open `ipsec_traffic.pcap` in Wireshark.  
2. Use the following **display filters**:

   * **IKE Phase 1 & 2:** `udp.port == 500 or udp.port == 4500`  
   * **ESP packets:** `esp`  
   * **AH packets:** `ah`

### Decrypting ESP (Optional)

1. Wireshark ▸ *Edit ▸ Preferences ▸ Protocols ▸ ESP*.  
2. Enter *SPI*, *Encryption Key*, *Authentication Key* obtained via `ip xfrm state`.

3. After adding, encrypted payloads turn into original IP packet contents.

---

## 4. Questions

1. What is the SPI value used?  
2. Is transport or tunnel mode employed?  (Look at inner/outer IP headers.)  
3. Which encryption & integrity algorithms negotiated? (IKE_SA_INIT)

---

## 5. Deliverables

• Annotated screenshot of one ESP and one AH packet header.  
• Answers to above questions.  
• `ipsec_traffic.pcap` file.

Good luck dissecting secure packets! 
