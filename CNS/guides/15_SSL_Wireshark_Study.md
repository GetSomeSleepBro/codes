# Lab 15 – Studying the SSL / TLS Protocol with Wireshark

Purpose: Capture and dissect a TLS 1.2 / 1.3 handshake while visiting an SSL-secured website (e.g., https://amazon.com).

---

## 1. Environment Setup

* Latest **Wireshark** (≥3.6).  
* **Firefox / Chrome** with *SSLKEYLOGFILE* environment variable (optional for decryption).

### Enabling SSL Key Logging (Optional but cool)

1. Create an empty file, e.g., `~/tls.keys`.  
2. Linux/macOS:

   ```bash
   export SSLKEYLOGFILE=~/tls.keys
   firefox &
   ```

3. Windows PowerShell:

   ```powershell
   setx SSLKEYLOGFILE "C:\Users\<user>\tls.keys"
   ```

4. In Wireshark: *Edit ▸ Preferences ▸ Protocols ▸ TLS ▸ (Pre)-Master-Secret log filename* → browse to `tls.keys`.

---

## 2. Capture Steps

1. Start Wireshark on the active interface.  
2. Display filter `tls` (new) or `ssl` (legacy) to watch only TLS frames.  
3. Visit your chosen HTTPS site and wait until it loads.  
4. Stop capture and save as `tls_handshake.pcapng`.

---

## 3. Analyse the Handshake

Look for the following packets (Use “No.” column):

1. **ClientHello** – cipher suites, TLS version.  
2. **ServerHello** – selected suite, random.  
3. **Certificate** – server cert chain.  
4. **Server Key Exchange** (if ECDHE).  
5. **Client Key Exchange** (TLS ≤1.2).  
6. **ChangeCipherSpec** (both directions).  
7. **Finished** messages.

> Use *Follow ▸ TLS Stream* to view decrypted HTTP/2 (if key log enabled).

---

## 4. Questions to Answer (include in report)

1. Which TLS version and cipher suite were negotiated?  
2. How many round-trips before encrypted application data?  
3. Size (bytes) of certificate chain?  
4. Did the server support Session Tickets / Resumption? (Look for `NewSessionTicket`)

---

## 5. Pro Tip – Filter Macros

Add to *Analyze ▸ Display Filter Macros*:

| Macro | Value |
|-------|-------|
| `tls.handshake` | `tls.handshake.type` |
| `tls.data` | `tls.record.content_type == 23` |

Then quickly filter with `${tls.handshake}`.

Happy decrypting! 
