#!/usr/bin/python3

import nmap

# Initialize the port scanner
scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

# Prompt the user to input the IP address to scan
ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)

# Prompt the user to select the type of scan to execute
resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan\n""")
print("You have selected option: ", resp)

# Prompt the user to input the port range to scan
port_range = input("Enter the port range you want to scan (e.g., 1-50): ")

# Execute the scan based on user input
if resp == '1':
    # Perform a SYN ACK scan
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print("Protocols: ", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    # Perform a UDP scan
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print("Protocols: ", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    # Perform a comprehensive scan
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port_range, '-v -sS -sU -sV -sC -A')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print("Protocols: ", scanner[ip_addr].all_protocols())
    # Check for open TCP and UDP ports and print them
    if 'tcp' in scanner[ip_addr].all_protocols():
        print("Open TCP Ports: ", scanner[ip_addr]['tcp'].keys())
    if 'udp' in scanner[ip_addr].all_protocols():
        print("Open UDP Ports: ", scanner[ip_addr]['udp'].keys())
else:
    # Handle invalid options
    print("Please enter a valid option")
