# Lab 12 – Installing & Configuring a DHCP Server

You’ll install **ISC DHCP Server** on Ubuntu Server (or Debian) and configure it to hand out IPv4 addresses.  Afterwards, use the provided `remote_install.py` to automate installation on a secondary machine via SSH.

---

## 1. Manual Installation (Local)

```bash
sudo apt update
sudo apt install isc-dhcp-server -y
```

On RPM-based systems use:

```bash
sudo yum install dhcp -y
```

---

## 2. DHCP Configuration – `/etc/dhcp/dhcpd.conf`

```conf
# option definitions common to all subnets
option domain-name "example.local";
option domain-name-servers 8.8.8.8, 8.8.4.4;

default-lease-time 600;
max-lease-time 7200;

subnet 192.168.10.0 netmask 255.255.255.0 {
    range 192.168.10.50 192.168.10.200;
    option routers 192.168.10.1;
    option broadcast-address 192.168.10.255;
}

host printer {
    hardware ethernet 00:11:22:33:44:55;
    fixed-address 192.168.10.10;
}
```

Enable interface in `/etc/default/isc-dhcp-server`:

```bash
INTERFACESv4="eth0"
```

Restart service:

```bash
sudo systemctl restart isc-dhcp-server
sudo systemctl status isc-dhcp-server
```

— You should see *active (running)*.

---

## 3. Testing

1. On a client PC set IPv4 to **DHCP / Automatic**.  
2. Run `ip addr` (Linux) or `ipconfig /all` (Windows) – you should get an address in 192.168.10.0/24.

3. View leases on the server:

```bash
grep -E "^lease" /var/lib/dhcp/dhcpd.leases
```

---

## 4. Remote Automated Install

Use the earlier **remote_install.py** script:

```bash
python programs/remote_install.py user@192.168.56.20 isc-dhcp-server
```

Script flow:

1. SSH into target.  
2. Detect package manager.  
3. Executes `sudo apt -y install isc-dhcp-server`.  
4. You then SCP or Git-push your `dhcpd.conf`, restart service, and you’re done.

---

## 5. Deliverables

* Screenshot of DHCP lease on client.  
* `dhcpd.conf` file.  
* Command line showing automated install.

Enjoy dynamic addressing! 
