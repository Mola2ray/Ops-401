#!/usr/bin/python3
# Lamin Touray
# Scripts: Prompt the user to type in a file name to search for.
# Prompt the user for a directory to search in.
# Search each file in the directory by name
# For each positive detection, print to the screen the file name and location.
# At the end of the search process, print to the screen how many files were searched and how many hits were found.


import os

# Prompt the user for input
file_to_search = input("Enter the file name to search for: ")
directory_to_search = input("Enter the directory to search in: ")

# Initialize counts
files_searched = 0
hits_found = 0

# Walk through the directory
for dirpath, dirnames, filenames in os.walk(directory_to_search):
    for filename in filenames:
        files_searched += 1
        if filename == file_to_search:
            hits_found += 1
            print(f"Found {file_to_search} in {os.path.join(dirpath, filename)}")

# Print the summary
print(f"Searched {files_searched} files.")
print(f"Found {hits_found} hits.")
