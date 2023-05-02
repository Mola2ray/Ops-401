#!/usr/bin/python3
# Lamin Touray
# Scripts:In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:

# Utilize the scapy library
# Define host IP
# Define port range or specific set of ports to scan
# Test each port in the specified range using a for loop
# If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
# If flag 0x14 received, notify user the port is closed.
# If no flag is received, notify the user the port is filtered and silently dropped.


from scapy.all import sr1, IP, TCP
import sys

# Define host IP and port range
host_ip = "192.168.1.1"
port_range = range(1, 1025)  # You can define your own range or specific set of ports

# Function to scan a port
def tcp_port_scan(host, port):
    # Create a SYN packet
    syn_packet = IP(dst=host) / TCP(dport=port, flags="S")

    # Send the packet and receive the response
    response = sr1(syn_packet, timeout=2, verbose=0)

    if response is None:
        print(f"Port {port}: Filtered (Silently dropped)")
    elif response.haslayer(TCP):
        tcp_layer = response.getlayer(TCP)
        if tcp_layer.flags == 0x12:  # SYN-ACK
            # Send a RST packet to close the connection
            rst_packet = IP(dst=host) / TCP(dport=port, flags="R")
            send(rst_packet, verbose=0)
            print(f"Port {port}: Open")
        elif tcp_layer.flags == 0x14:  # RST-ACK
            print(f"Port {port}: Closed")
    else:
        print(f"Port {port}: Unexpected response")

# Scan each port in the specified range
for port in port_range:
    tcp_port_scan(host_ip, port)
