#!/usr/bin/python3
# Lamin Touray
# Scripts: Prompts the user to type a URL or IP address.
# Prompts the user to type a port number.
# Performs banner grabbing using netcat against the target address at the target port; prints the results to the screen then moves on to the step below.
# Performs banner grabbing using telnet against the target address at the target port; prints the results to the screen then moves on to the step below.
# Performs banner grabbing using Nmap against the target address of all well-known ports; prints the results to the screen.


import subprocess
import shlex

# Prompt the user for the target IP address or URL and the port number
target = input("Please enter a URL or IP address: ")
port = input("Please enter a port number: ")

# Define the netcat, telnet, and nmap commands to be used for banner grabbing
# Netcat and Telnet will be used on the user-specified port, 
# whereas Nmap will be used on all well-known ports.
netcat_cmd = f'nc -v -n {target} {port}'
telnet_cmd = f'telnet {target} {port}'
nmap_cmd = f'nmap -p- --script=banner {target}'

# Execute the commands using subprocess module
for cmd in [netcat_cmd, telnet_cmd, nmap_cmd]:
    print(f"\nExecuting: {cmd}")

    # Create a new process, connect its pipes to Python’s, and start it.
    # The shlex.split function splits the command string into a sequence that the subprocess can understand.
    process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Communicate with the process: Send data to stdin, close it, and wait for the process to exit.
    # A tuple (stdoutdata, stderrdata) is returned.
    output, _ = process.communicate()

    # Print the output of the command execution
    print(f"\nResults:\n{output.decode('utf-8')}")

# Source: chatGPT
