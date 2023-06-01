#!/usr/bin/python3
# Lamin Touray
# Scripts:Continue developing your Python malware detection tool.
# Alter your search code to recursively scan each file and folder in the user input directory path and print it to the screen.
# For each file scanned within the scope of your search directory:
# Generate the file’s MD5 hash using Hashlib.
# Assign the MD5 hash to a variable.
# Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.


import os
import hashlib
import time

# Prompt the user for input
directory_to_search = input("Enter the directory to search in: ")

# Walk through the directory
for dirpath, dirnames, filenames in os.walk(directory_to_search):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)

        # Skip symbolic links
        if not os.path.islink(file_path):
            with open(file_path, 'rb') as file:
                data = file.read()
                md5_hash = hashlib.md5(data).hexdigest()

            file_size = os.path.getsize(file_path)
            timestamp = time.ctime(os.path.getmtime(file_path))

            print(f"Timestamp: {timestamp}, File Name: {filename}, File Size: {file_size} bytes, "
                  f"Path: {file_path}, MD5: {md5_hash}")


# Source: chatGPT

