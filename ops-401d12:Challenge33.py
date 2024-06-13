#!/usr/bin/env python3

# Script Name:                  Ops Challenge: Signature-based Malware Detection Part 2 of 3
# Author:                       Cody Blahnik
# Date of latest revision:      06/11/24
# Purpose:                      Scan files for malware using VirusTotal API

import os
import hashlib
import logging
import requests
from datetime import datetime

API_KEY_VIRUSTOTAL = "65ad0b914436ba7a2f05c8cb7621837c903e19b95a21a33265dfddda8453f339"

# Set up logging
logging.basicConfig(filename='file_scan.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def calculate_md5(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
        return None

def query_virustotal(api_key, file_hash):
    url = f'https://www.virustotal.com/api/v3/files/{file_hash}'
    headers = {
        'x-apikey': api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"VirusTotal API error: {response.status_code} - {response.text}")
        return None

def scan_directory(search_directory):
    """Recursively scan each file and folder in the directory."""
    results = []
    
    for root, dirs, files in os.walk(search_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            md5_hash = calculate_md5(file_path)
            
            if md5_hash:
                result = {
                    'timestamp': timestamp,
                    'file_path': file_path,
                    'file_name': file,
                    'file_size': file_size,
                    'md5_hash': md5_hash
                }
                results.append(result)
                # Print to screen
                print(f"{timestamp} | {file_path} | {file} | {file_size} bytes | MD5: {md5_hash}")
                # Log the result
                logging.info(f"{timestamp} | {file_path} | {file} | {file_size} bytes | MD5: {md5_hash}")
                
                # Query VirusTotal
                vt_result = query_virustotal(API_KEY_VIRUSTOTAL, md5_hash)
                if vt_result:
                    # Handle and log the VirusTotal result
                    vt_summary = vt_result.get('data', {}).get('attributes', {}).get('last_analysis_stats', {})
                    logging.info(f"VirusTotal result for {file_path}: {vt_summary}")
                    print(f"VirusTotal result for {file_path}: {vt_summary}")
    
    return results

def main():
    # Prompt user for directory
    search_directory = input("Enter the directory to scan: ").strip()

    # Validate directory
    if not os.path.isdir(search_directory):
        print(f"Error: {search_directory} is not a valid directory.")
        logging.error(f"{search_directory} is not a valid directory.")
        return

    logging.info(f"Starting scan in directory '{search_directory}'")

    # Perform the scan
    results = scan_directory(search_directory)

    # Print summary
    print(f"\nScan complete. {len(results)} files were scanned.")
    logging.info(f"Scan complete. {len(results)} files were scanned.")

if __name__ == "__main__":
    main()
