#!/usr/bin/python3
# Lamin Touray
# Scripts:


import subprocess
import ipaddress

# Prompt user for network address and CIDR block
network_address = input("Enter network address with CIDR block (e.g. 10.0.0.0/24): ")
network = ipaddress.ip_network(network_address, strict=False)

# Define variables to keep track of number of hosts
total_hosts = 0
online_hosts = 0

# Loop through each IP address in the network
for ip in network.hosts():
    total_hosts += 1
    ip_address = str(ip)
    
    # Skip the network address and broadcast address
    if ip_address == str(network.network_address) or ip_address == str(network.broadcast_address):
        continue
    
    # Ping the host and capture output
    ping_output = subprocess.run(["ping", "-c", "1", "-W", "2", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
    # Check the output for indications of a live host
    if "1 received" in ping_output.stdout:
        print(f"{ip_address} is online")
        online_hosts += 1
    elif "100% packet loss" in ping_output.stderr:
        print(f"{ip_address} is down or unresponsive")
    elif "ICMP type 3" in ping_output.stderr and any(code in ping_output.stderr for code in ["1", "2", "3", "9", "10", "13"]):
        print(f"{ip_address} is actively blocking ICMP traffic")
    else:
        print(f"{ip_address} is responding but with an unknown ICMP type or code")
        
# Print the total number of hosts and how many are online
print(f"Scanned {total_hosts} hosts in the network. {online_hosts} hosts are online.")
