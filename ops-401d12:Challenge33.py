#!/usr/bin/env python3

# Script Name:                  Ops Challenge: Signature-based Malware Detection Part 2 of 3
# Author:                       Cody Blahnik
# Date of latest revision:      06/11/24
# Purpose:                      Scan files for malware using VirusTotal API

import os
import hashlib
import logging
import requests
import time
from datetime import datetime

# Retrieve API key from environment variable (set it beforehand for security)
API_KEY_VIRUSTOTAL = os.getenv("VIRUSTOTAL_API_KEY")

# Check if API key is set
if not API_KEY_VIRUSTOTAL:
    raise ValueError("Error: VirusTotal API key is missing. Set the environment variable 'VIRUSTOTAL_API_KEY'.")

# Set up logging
LOG_FILE = "file_scan.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

def calculate_md5(file_path):
    """Calculate the MD5 hash of a file efficiently."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
        return None

def query_virustotal(file_hash):
    """Query VirusTotal for file hash analysis."""
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": API_KEY_VIRUSTOTAL}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"VirusTotal API request error for {file_hash}: {e}")
        return None

def scan_directory(search_directory):
    """Recursively scan files in the directory and query VirusTotal."""
    results = []
    
    for root, _, files in os.walk(search_directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Skip empty or unreadable files
            if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
                continue

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            md5_hash = calculate_md5(file_path)

            if md5_hash:
                result = {
                    "timestamp": timestamp,
                    "file_path": file_path,
                    "file_name": file,
                    "md5_hash": md5_hash,
                }
                results.append(result)

                # Log & display file details
                log_msg = f"{timestamp} | {file_path} | {file} | MD5: {md5_hash}"
                print(log_msg)
                logging.info(log_msg)

                # Query VirusTotal
                vt_result = query_virustotal(md5_hash)
                if vt_result:
                    vt_summary = vt_result.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
                    logging.info(f"VirusTotal result for {file_path}: {vt_summary}")
                    print(f"VirusTotal result for {file_path}: {vt_summary}")
                
                # Rate limit to avoid exceeding API quota (optional)
                time.sleep(15)

    return results

def main():
    """Main function to execute file scanning."""
    search_directory = input("Enter the directory to scan: ").strip()

    if not os.path.isdir(search_directory):
        print(f"Error: '{search_directory}' is not a valid directory.")
        logging.error(f"Invalid directory: {search_directory}")
        return

    logging.info(f"Starting scan in directory '{search_directory}'")
    results = scan_directory(search_directory)
    print(f"\nScan complete. {len(results)} files were scanned.")
    logging.info(f"Scan complete. {len(results)} files scanned.")

if __name__ == "__main__":
    main()
