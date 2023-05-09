#!/usr/bin/env python3
# Lamin Touray

#In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

#The script must:

#Transmit a single ICMP (ping) packet to a specific IP every two seconds.
#Evaluate the response as either success or failure.
#Assign success or failure to a status variable.
#For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
#Example output: 2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

import subprocess
import time
import datetime

# Define the IP address to ping
ip = "192.168.1.1"

# Define the interval between pings (in seconds)
interval = 2

# Main loop
while True:
    # Ping the IP address
    ping = subprocess.Popen(
        ["ping", "-c", "1", "-W", "1", ip],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, error = ping.communicate()

    # Evaluate the response
    if "1 received" in out.decode("utf-8"):
        status = "Network Active"
    else:
        status = "Network Inactive"

    # Print the result with a timestamp
    print(
        f"{datetime.datetime.now()} {status} to {ip}"
    )

    # Wait for the specified interval
    time.sleep(interval)


# Sources: chatGPT