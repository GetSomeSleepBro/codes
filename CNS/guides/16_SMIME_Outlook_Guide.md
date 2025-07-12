# Lab 16 – Implementing S/MIME Email Security in Microsoft Outlook

Secure/Multipurpose Internet Mail Extensions (S/MIME) provides end-to-end e-mail encryption and digital signatures using X.509 certificates.

---

## 1. Prerequisites

| Item | Notes |
|------|-------|
| Microsoft Outlook 2016/2019/365 | Same steps for newer versions |
| Personal S/MIME certificate | Obtain from a CA (e.g., Sectigo, DigiCert) or create self-signed via OpenSSL for lab |
| Access to mail server (IMAP/SMTP or Exchange) |

### Generating a Self-Signed Cert (Optional)

```bash
openssl req -x509 -newkey rsa:2048 -keyout smime.key -out smime.crt -days 365 -nodes -subj "/CN=Student/O=College"
openssl pkcs12 -export -inkey smime.key -in smime.crt -out smime.p12 -name "Student S/MIME"
```

---

## 2. Import Certificate into Windows

1. Double-click `smime.p12`.  
2. Certificate Import Wizard → store in **Personal**.  
3. Provide export password if prompted.

---

## 3. Configure Outlook

1. File ▸ Options ▸ Trust Center ▸ **Trust Center Settings**.  
2. Click **Email Security**.  
3. Under *Encrypted e-mail* → **Settings…**.
   * Choose your certificate (it reads from Personal store).  
   * Encryption algorithm: AES256.  
   * Hash algorithm: SHA-256.
4. Tick “Add digital signature to outgoing messages”.  
5. Tick “Encrypt contents and attachments for outgoing messages” if you want default encryption.

---

## 4. Sending a Signed / Encrypted Email

1. New Email ▸ Options tab:  
   * **Sign** (✓)  
   * **Encrypt** (lock icon) – choose *Encrypt with S/MIME*.
2. Send to a classmate who has also exchanged S/MIME certs.

---

## 5. Receiving & Verifying

When you receive a signed email, Outlook shows a red ribbon icon. Click it → **Digital Signature Details** to verify:

• Issuer CA, validity dates  
• Hash algorithm  
• “Signature is valid.”

For encrypted mail, Outlook automatically decrypts using your private key.

---

## 6. Common Issues & Fixes

| Problem | Solution |
|---------|----------|
| “No certificate associated with this e-mail account” | Import cert into Personal store and restart Outlook |
| Recipient cannot decrypt | Ensure you have exchanged **public** certificates (send a signed e-mail first) |
| Self-signed cert not trusted | Recipient must import your cert into **Trusted People** |

---

## 7. Deliverables

• Screenshot of signed & encrypted e-mail icons.  
• Certificate details window showing SHA-256 and validity.  
• Short paragraph on why S/MIME is end-to-end whereas TLS is hop-by-hop.

Congratulations – your e-mails are now confidential and authenticated! 
