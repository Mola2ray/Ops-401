#!/usr/bin/python3
# Lamin Touray
# Scripts: add a new mode to your Python brute force tool that allows you to brute force attack a password-locked zip file.
# Use the zipfile library.
# Pass it the RockYou.txt list to test all words in the list against the password-locked zip file.




import zipfile

# Define the function for offensive mode
def offensive_mode():
    # Prompt the user to enter the path to the word list file
    wordlist_file = input("Enter the path to the word list file: ")
    # Open the file and iterate through each line (i.e. each word)
    with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            # Strip any newline characters from the line and assign the resulting string to a variable
            password = line.strip()
            # Attempt to extract the zip file with the current password
            try:
                with zipfile.ZipFile("locked_file.zip") as zip_file:
                    zip_file.extractall(pwd=password.encode())
                    print(f"Password found: {password}")
                    return
            except:
                # If the password is incorrect, continue to the next password
                pass

    # If no password was found in the word list, print a message to the console
    print("Password not found in word list.")

# Define the function for defensive mode
def defensive_mode():
    # Prompt the user to enter a string to search for and the path to the word list file
    user_input = input("Enter a string to search: ")
    wordlist_file = input("Enter the path to the word list file: ")
    # Open the file and iterate through each line (i.e. each word)
    with open(wordlist_file, "r") as f:
        for line in f:
            # Check if the user input string is found in the current line/word
            if user_input in line:
                # If the string is found, print a message to the console and exit the function
                print(f"{user_input} was found in the word list.")
                return
        # If the string was not found in any of the words, print a message to the console
        print(f"{user_input} was not found in the word list.")

# Define the function for brute forcing a password-locked zip file
def brute_force_zip(zip_file_path, wordlist_file_path):
    # Open the zip file
    with zipfile.ZipFile(zip_file_path, "r") as zip_file:
        # Prompt the user to enter the path to the word list file
        wordlist_file = open(wordlist_file_path, "r", encoding="utf-8", errors="ignore")
        # Iterate through each line (i.e. each word) in the word list
        for line in wordlist_file:
            # Strip any newline characters from the line and assign the resulting string to a variable
            password = line.strip()
            # Attempt to extract the zip file with the current password
            try:
                zip_file.extractall(pwd=password.encode())
                print(f"Password found: {password}")
                return
            except:
                # If the password is incorrect, continue to the next password
                pass

    # If no password was found in the word list, print a message to the console
    print("Password not found in word list.")

# Prompt the user to select a mode (offensive, defensive, or brute force zip)
mode = input("Select a mode (1 for offensive, 2 for defensive, 3 for brute force zip): ")
# Call the appropriate function based on the user's selection
if mode == "1":
    offensive_mode()
elif mode == "2":
    defensive_mode()
elif mode == "3":
    zip_file_path = input("Enter the path to the password-locked zip file: ")
    wordlist_file_path = input("Enter the path to the word list file: ")
