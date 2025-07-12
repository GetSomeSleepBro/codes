#!/usr/bin/env python3
"""
Remote Package Installer (SSH)
-----------------------------
Connects to a remote Linux machine via SSH and installs a package using the
system package manager (supports *apt* and *yum*). Requires the *paramiko*
library to be installed locally.

Usage:
    $ python remote_install.py <user>@<host> package_name [--password XXX]

Example:
    $ python remote_install.py admin@192.168.1.10 isc-dhcp-server --password secret

Disclaimer:
    • SSH credentials travel in clear text on the command line; prefer SSH keys.
    • The script is a minimal demonstration and lacks robust error handling.
"""

import argparse
import getpass
import sys


def main():
    try:
        import paramiko
    except ImportError:
        print("This script requires the 'paramiko' library. Install with 'pip install paramiko'.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Install a package via SSH on a remote host")
    parser.add_argument("target", help="Target in the form user@host or host (defaults to current user)")
    parser.add_argument("package", help="Package name to install, e.g., isc-dhcp-server")
    parser.add_argument("--password", help="Password for SSH (omit when key-based auth is configured)")
    args = parser.parse_args()

    if '@' in args.target:
        user, host = args.target.split('@', 1)
    else:
        import getpass as _gp
        user = _gp.getuser()
        host = args.target

    passwd = args.password or getpass.getpass(f"Password for {user}@{host}: ")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Connecting to {host} ...")
    ssh.connect(host, username=user, password=passwd)

    # Detect package manager
    stdin, stdout, _ = ssh.exec_command("which apt || which yum")
    mgr_path = stdout.readline().strip()
    if not mgr_path:
        print("Could not detect apt or yum on remote host.")
        return
    mgr = 'apt' if 'apt' in mgr_path else 'yum'

    cmd = f"sudo {mgr} -y install {args.package}"
    print("Running:", cmd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print("Errors:\n", err)
    else:
        print("Installation complete.")

    ssh.close()


if __name__ == "__main__":
    main()
