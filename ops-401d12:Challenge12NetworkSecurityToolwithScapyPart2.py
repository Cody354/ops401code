#!/usr/bin/env python3

# Script Name:                  ops-401d1:Challenge11NetworkSecurityToolwithScapyPart1.py
# Author:                       Cody Blahnik
# Date of latest revision:      5/13/24
# Purpose:                      creating our own network scanning tool
# Informational websites:       https://www.freecodecamp.org/news/python-print-exception-how-to-try-except-print-an-error/


#Utilize the scapy library
import sys
import ipaddress
from scapy.all import sr1, IP, ICMP, TCP
#Define host IP
ip = input("What IP would you like to use?")
#Define port range or specific set of ports to scan
ports = input("what port would you like to scan?")
#Test each port in the specified range using a for loop
for port in ports.split(","):
    #Creating a packet
    packet = IP(dst=ip) / TCP(dport=int(port), flags="S")
    #Creating a response packet
    response = sr1(packet, timeout=1, verbose=0)

    #Checking inputs from users
    if response:
        #sending a ping to the ip on
        if response.haslayer(TCP) and response[TCP].flags == 0x12:
            print(f"Port {port}: Open")
            #If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
            rst_packet = IP(dst=ip) / TCP(dport=int(port), flags="R")
            rst_response = sr1(rst_packet, timeout=1, verbose=0)
            print(f"RST sent to close connection on port {port}")
        #If flag 0x14 RST received, the port is closed
        elif response.haslayer(TCP) and response[TCP].flags == 0x14:
            print(f"Port {port}: Closed")
        else:
            #If no flag is received, notify the user the port is filtered and silently dropped
            print(f"Port {port}: Filtered (Silently Dropped)")
    else:
        #If no response was received, the port is filtered
        print(f"Port {port}: Filtered")
# Pinging the CIDR bloc
def icmp_ping_sweep():
    network = input("Enter the network address with CIDR block (e.g., 10.10.0.0/24): ")
    # testing the user input.
    try:
        network = ipaddress.ip_network(network, strict=False)
    except ValueError as e:
        print(f"Invalid network address: {e}")
        return

    live_hosts = 0
    #Function for pining user input.
    for ip in network.hosts():
        print(f"Pinging {ip} - please wait...")
        response = sr1(IP(dst=str(ip)) / ICMP(), timeout=2, verbose=0)

        if response and response.haslayer(ICMP):
            icmp_type, icmp_code = response[ICMP].type, response[ICMP].code
            if icmp_type == 0:
                print(f"Host {ip} is responding.")
                live_hosts += 1
            elif icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
                print(f"Host {ip} is actively blocking ICMP traffic.")
            else:
                print(f"Host {ip} is unresponsive.")
        else:
            print(f"Host {ip} is unresponsive.")

    print(f"Total live hosts: {live_hosts}")
#asking the user what they want todo
def main():
    print("Network Security Tool")
    print("1. TCP Port Range Scanner")
    print("2. ICMP Ping Sweep")
    choice = input("Select an option (1 or 2): ")

    if choice == '1':
        tcp_port_scan()
    elif choice == '2':
        icmp_ping_sweep()
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()

print(response)