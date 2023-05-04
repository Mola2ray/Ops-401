#!/usr/bin/python3
# Lamin Touray
# Scripts:In Python, combine the two modes (port and ping) of your network scanner script.
# Eliminate the choice of mode selection.
# Continue to prompt the user for an IP address to target.
# Move port scan to its own function.
# Call the port scan function if the host is responsive to ICMP echo requests.
# Print the output to the screen


import socket
import subprocess

# Define a function to check if the host is up by sending an ICMP echo request
def ping_host(ip_address):
    ping_response = subprocess.call(['ping', '-c', '1', '-W', '1', ip_address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return ping_response == 0

# Define a function to scan for open ports on the target IP address
def port_scan(ip_address):
    open_ports = []
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Prompt the user for an IP address to target
ip_address = input("Enter an IP address to scan: ")

# Check if the host is up by sending an ICMP echo request
if ping_host(ip_address):
    # If the host is up, perform a port scan
    open_ports = port_scan(ip_address)
    if len(open_ports) > 0:
        print(f"The following ports are open on {ip_address}: {', '.join(map(str, open_ports))}")
    else:
        print(f"No open ports found on {ip_address}.")
else:
    print(f"{ip_address} is down.")
