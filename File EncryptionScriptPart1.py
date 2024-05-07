# Import the Fernet class from the cryptography.fernet module
from cryptography.fernet import Fernet

# Import the os module
import os

# generate a key using the Fernet
key = Fernet.generate_key()

# Asigin the key to cipher_suite
cipher_suite = Fernet(key)

# declare a function to encrypt the file
def encrypt_file(file_path):
    # Open the file 
    with open(file_path, 'rb') as f:
        # Read the contents of the file
        plaintext = f.read()
    # Encrypt the document
    encrypted_text = cipher_suite.encrypt(plaintext)
    # Open the file
    with open(file_path, 'wb') as f:
        # Write the encrypted text back to the file
        f.write(encrypted_text)

# Declare a function to decrypt a file 
def decrypt_file(file_path):
    # Open the fil
    with open(file_path, 'rb') as f:
        # Read the encrypted text 
        encrypted_text = f.read()
    # Decrypt the encrypted text
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    # Open the file
    with open(file_path, 'wb') as f:
        # Write the decrypted text back to the file
        f.write(decrypted_text)

# Define a function to encrypt a message
def encrypt_message(message):
    # Encrypt the message
    encrypted_text = cipher_suite.encrypt(message.encode())
    # Print the encrypted message
    print("Encrypted message:", encrypted_text.decode())

# Define a function to decrypt a message
def decrypt_message(message):
    # Decrypt the message\
    decrypted_text = cipher_suite.decrypt(message.encode())
    # Print the decrypted message
    print("Decrypted message:", decrypted_text.decode())

# Main function for user input
def main():
    # Print options for the user
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    
    # Prompt the user to enter a mode
    mode = input("Enter mode: ")
    
    # Check the selected mod
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
        message = input("Enter the message to encrypt: ")
        encrypt_message(message)
    elif mode == '4':
        message = input("Enter the message to decrypt: ")
        decrypt_message(message)
    else:
        print("Invalid mode.")
if __name__ == "__main__":
    main()
