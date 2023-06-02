#!/usr/bin/python3
# Lamin Touray
# Scripts:   Successfully connect to the VirusTotal API
# Automatically compare your target file’s md5 hash with the hash values of entries on VirusTotal API
# Print to the screen the number of positives detected and total files scanned
# The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.


import os
import hashlib
import time
import requests

# VirusTotal API Endpoint
url = 'https://www.virustotal.com/api/v3/files/'

# Prompt the user for input
directory_to_search = input("Enter the directory to search in: ")

# Prompt for API key
api_key = input("Enter your VirusTotal API key: ")
headers = {
  "x-apikey": api_key
}

# Initialize counts
files_scanned = 0
positives = 0

# Walk through the directory
for dirpath, dirnames, filenames in os.walk(directory_to_search):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)

        # Skip symbolic links
        if not os.path.islink(file_path):
            with open(file_path, 'rb') as file:
                data = file.read()
                md5_hash = hashlib.md5(data).hexdigest()

            # Compare with VirusTotal
            response = requests.get(url + md5_hash, headers=headers)

            if response.status_code == 200:
                report = response.json()
                if report['data']['attributes']['last_analysis_stats']['malicious'] > 0:
                    positives += 1

            files_scanned += 1

# Print the summary
print(f"Scanned {files_scanned} files.")
print(f"Found {positives} positives.")
