#!/usr/bin/env python3

# Script Name:                  ops-401d1:Challenge11NetworkSecurityToolwithScapyPart1.py
# Author:                       Cody Blahnik
# Date of latest revision:      5/13/24
# Purpose:                      creating our own network scanning tool


#Utilize the scapy library
import sys
from scapy.all import srp, sr1, IP, ICMP
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
        #sending a ping to the ip on flag 12
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
