# Lab 13 – Targeted Packet Capture & Analysis with Wireshark

> Objective: Capture specific Facebook traffic and analyse TCP flags.  This lab assumes you are capturing on your *own* device and complying with your institution’s usage policy.

---

## 1. Capture Filters vs Display Filters

* **Capture filter** – applied by libpcap/BPF, discards unwanted packets **before** they hit Wireshark. Set in the *“Capture Options”* window.
* **Display filter** – applied after capture; can be changed anytime.

---

## 2. Filter Expressions for the Assignment

### 2.1 All TCP traffic to/from Facebook while logging in

1. Resolve Facebook’s IPs prior to capture:

   ```bash
   nslookup facebook.com | grep Address
   ```

   Typically returns 31.13.71.36, etc.  Use *all* resolved IPs.

2. **Capture filter** (example for two IPs):

   ```
   host 31.13.71.36 or host 157.240.229.35 and tcp
   ```

   Alternatively filter by subnet: `net 31.13.64.0/18 and tcp`.

### 2.2 All HTTP traffic to/from Facebook

Facebook forces HTTPS, but assume lab wants port 80:

```
tcp port 80 and (host 31.13.71.36 or host 157.240.229.35)
```

### 2.3 Display filter – count SYN, PSH, RST flags

Start from capture #1 (TCP only). Use:

```
tcp.flags.syn == 1
tcp.flags.push == 1
tcp.flags.reset == 1
```

Menu ▸ **Statistics ▸ Summary** shows total packets; apply each filter and note “Displayed”. Compute fraction = displayed / total.

### 2.4 Number of TCP packets vs HTTP packets

* **All TCP** (already captured) – Wireshark shows total.  
* **HTTP subset** – Display filter: `http`.  
* Statistics ▸ **Endpoints** ▸ “IPv4” tab: Select Facebook IP, note *Packets* column.

---

## 3. Saving the Capture

File ▸ Save As ▸ `facebook_login.pcapng`. Provide along with a `.txt` report containing counts/fractions.

---

## 4. Common Pitfalls

| Issue | Fix |
|-------|-----|
| "No interfaces found" | Run Wireshark as Administrator or add user to *wireshark* Linux group |
| Packets still encrypted | That’s expected with HTTPS; use `ssl.keylog_file` + browser env var for decryption (advanced) |

Happy capturing! 
