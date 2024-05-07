!#bin/bash/env python3

# Script Name:                 FileEncryptionScriptPart2
# Author:                       Cody Blahnik
# Date of latest revision:      3/7/24
# Purpose:                      encrpyts fiels


# Write a script that:
# Creates four directories: dir1, dir2, dir3, dir4




# Import necessary modules
from cryptography.fernet import Fernet  # Import the Fernet class from the cryptography.fernet module
import os  # Import the os module

# Generate a key using Fernet
key = Fernet.generate_key()

# Assign the key to cipher_suite
cipher_suite = Fernet(key)

# Function to encrypt a file
def encrypt_file(file_path):
    # Open the file in binary mode for reading
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    # encrypts text
    encrypted_text = cipher_suite.encrypt(plaintext)
    # Open the file
    with open(file_path, 'wb') as f:
        f.write(encrypted_text)

# Function to decrypt a file
def decrypt_file(file_path):
    # Open the file in binary mode for reading
    with open(file_path, 'rb') as f:
        # Read the encrypted text from the file
        encrypted_text = f.read()
    # Decrypt the encrypted text using the cipher_suite
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    # Open the file in binary mode for writing
    with open(file_path, 'wb') as f:
        # Write the decrypted text back to the file
        f.write(decrypted_text)

# function to recursively encrypt a folder 
def encrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Callfunction to
            encrypt_file(file_path)

# Function to recursively decrypt a folder that was encrypted by this tool
def decrypt_folder(folder_path):
    # Recursively iterate through all files and subdirectories in the folder
    for root, dirs, files in os.walk(folder_path):
        # Iterate through each file in the current directory
        for file in files:
            file_path = os.path.join(root, file)
            # Call function
            decrypt_file(file_path)

# user input
def main():
    # Print options for user
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a folder (and its contents)")
    print("4. Decrypt a folder (previously encrypted by this tool)")
    
    # Prompts user to enter a mode
    mode = input("Enter mode: ")
    
    # Check the mode
    if mode == '1':
        file_path = input("Enter the file path: ")
        if os.path.exists(file_path):
            encrypt_file(file_path)
            print("File encrypted successfully.")
        else:
            print("File not found.")
    elif mode == '2':
        file_path = input("Enter the file path: ")
        if os.path.exists(file_path):
            decrypt_file(file_path)
            print("File decrypted successfully.")
        else:
            print("File not found.")
    elif mode == '3':
        folder_path = input("Enter the folder path: ")
        if os.path.exists(folder_path):
            encrypt_folder(folder_path)
            print("Folder and its contents encrypted successfully.")
        else:
            print("Folder not found.")
    elif mode == '4':
        folder_path = input("Enter the folder path: ")
        if os.path.exists(folder_path):
            decrypt_folder(folder_path)
            print("Folder and its contents decrypted successfully.")
        else:
            print("Folder not found.")
    else:
        print("Invalid mode.")

if __name__ == "__main__":
    main()
