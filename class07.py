from cryptography.fernet import Fernet
import os

# Function to generate and save a new encryption key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the encryption key from file
def load_key():
    return open("key.key", "rb").read()

# Function to encrypt a single file
def encrypt_file(file_name, key):
    with open(file_name, "rb") as file:
        file_data = file.read()
    encryption = Fernet(key)
    encrypted = encryption.encrypt(file_data)
    with open(file_name, "wb") as file:
        file.write(encrypted)

# Function to decrypt a single file
def decrypt_file(file_name, key):
    with open(file_name, "rb") as file:
        file_data = file.read()
    decryption = Fernet(key)
    decrypted = decryption.decrypt(file_data)
    with open(file_name, "wb") as file:
        file.write(decrypted)

# Function to encrypt all files in a folder and its subdirectories
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Function to decrypt all files in a folder and its subdirectories
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

# Generate and save encryption key
write_key()
key = load_key()

print("Your key is: " + str(key.decode('utf-8')))

# Main loop to display the menu and handle user input
while True:
    menu = ["1: Encrypt a file", "2: Decrypt a file", "3: Encrypt a folder", "4: Decrypt a folder", "5: Exit"]
    for i in menu:
        print(i)
    mode = input("Please select a mode: ")

    if mode in ["1", "2", "3", "4"]:
        target = input("Enter file/folder name: ")

    if mode == "1":
        encrypt_file(target, key)
    elif mode == "2":
        decrypt_file(target, key)
    elif mode == "3":
        encrypt_folder(target, key)
    elif mode == "4":
        decrypt_folder(target, key)
    elif mode == "5":
        exit()
    else:
        print("Invalid input. Please try again.")

# Sources:Tyler & chaGPT