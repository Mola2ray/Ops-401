#!/usr/bin/python3
# Lamin Touray
# Scripts: prompts the user to select one of the following modes:
# Mode 1: Offensive; Dictionary Iterator
# Mode 2: Defensive; Password Recognized



import time

# Define the function for offensive mode
def offensive_mode():
    # Prompt the user to enter the path to the word list file
    wordlist_file = input("Enter the path to the word list file: ")
    # Open the file and iterate through each line (i.e. each word)
    with open(wordlist_file, "r") as f:
        for line in f:
            # Strip any newline characters from the line and assign the resulting string to a variable
            word = line.strip()
            # Print the word to the console
            print(word)
            # Add a delay of 0.5 seconds before processing the next word
            time.sleep(0.5)

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

# Prompt the user to select a mode (offensive or defensive)
mode = input("Select a mode (1 for offensive, 2 for defensive): ")
# Call the appropriate function based on the user's selection
if mode == "1":
    offensive_mode()
elif mode == "2":
    defensive_mode()
else:
    # If the user enters an invalid mode selection, print an error message to the console
    print("Invalid mode selected.")

# Source: chaGPT