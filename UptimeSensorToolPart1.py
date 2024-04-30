#!/usr/bin/env python3
# Script Name:                  Uptime Sensor Tool Part 1 
# Author:                       Cody Blahnik
# Date of latest revision:      4//30/2024
# Purpose:                      uptime sensor tool that checks systems are responding

# Import Ping & time 
import ping
import time
from datetime import datetime
# This function continuously pings a destination IP every 2 seconds and prints the status along with a timestamp.
# destination_ip (str): The IP address of the host to ping.
def uptime_sensor(destination_ip):
# THis is starting a whil loop
  while True:
    # Pinging disired ip
    response = ping.ping(destination_ip, verbose=False)
    # Checking if the statemnt is ture or false
    status = "Success" if response else "Failure"
    # fetching the time stamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Displaying the time stamp, the ip, and the status from the true or false.
    print(f"{timestamp} - {destination_ip}: {status}")
    time.sleep(2)
# A conditional statemnt checking the value name
if __name__ == "__main__":
  # Replace with the actual IP address of the host you want to monitor
  destination_ip = "192.168.1.10"
  uptime_sensor(destination_ip)
