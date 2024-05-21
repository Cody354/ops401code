
#!/usr/bin/env python3

# Script Name:                  ops-401d1:Challenge16AutomatedBruteForceWordlistAttackToolPart1.py
# Author:                       Cody Blahnik
# Date of latest revision:      5/20/24
# Purpose:                      Brute force tool using nltk

import nltk
import time

def get_words():
    nltk.download("words", quiet=True)
    word_list = words.words()
    return word_list
# checking user input for ovffensive task
def offensive():
    file_path = input("Enter the word list file path: ")
    delay = float(input("Enter the delay between words (in seconds): "))
    
    try:
        with open(file_path,encoding = "ISO-8859-1") as file:
            for word in file:
                word = word.strip()
                print(word)
                time.sleep(delay)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
# checking user input for deviseve 
def defensive():
    user_string = input("Enter the string to search for: ")
    file_path = input("Enter the word list file path: ")

    try:
        with open(file_path, encoding = "ISO-8859-1") as file:
            word_list = [word.strip() for word in file]
            
        if user_string in word_list:
            print(f"The string '{user_string}' was found in the word list.")
        else:
            print(f"The string '{user_string}' was NOT found in the word list.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
# the menu for the user
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
