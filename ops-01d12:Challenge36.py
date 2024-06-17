#!/usr/bin/env python3
# Script Name:                  Web Application Fingerprinting
# Author:                       Cody Blahnik
# Date of latest revision:      4//30/2024
# Purpose:                      multiple banner grabbing approaches against a single target


import socket
import subprocess
import re

def banner_grab(address, port, tool):
  """
  Performs banner grabbing using the specified tool.

  Args:
      address: The target IP address or URL.
      port: The target port number.
      tool: The tool to use for banner grabbing (netcat, telnet, nmap).

  Returns:
      A string containing the captured banner or an error message.
  """
  try:
    if tool == "netcat":
      # Use `nc` command with `-v` for verbose output
      result = subprocess.run(["nc", "-v", f"{address} {port}"], capture_output=True, text=True)
      return result.stdout.strip()
    elif tool == "telnet":
      # Open a Telnet socket and read the banner
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((address, port))
      banner = sock.recv(1024).decode()
      sock.close()
      return f"Telnet: {banner.strip()}"
    elif tool == "nmap":
      # Use `nmap` to scan a single port and capture output
      result = subprocess.run(["nmap", "-p", f"{port}", address], capture_output=True, text=True)
      # Extract relevant service information using regex (optional)
      match = re.search(r"PORT\s+(\d+)\s+tcp\s+open\s+(.+)", result.stdout)
      if match:
        service = match.group(2).strip()
        return f"Nmap: Port {match.group(1)} - {service}"
      else:
        return f"Nmap: No service information found."
    else:
      return f"Invalid tool: {tool}"
  except Exception as e:
    return f"Error with {tool}: {e}"

def main():
  """
  Prompts the user for input and performs banner grabbing.
  """
  while True:
    target = input("Enter target URL/IP: ")
    try:
      # Validate and convert port number to integer
      port = int(input("Enter port number: "))
      break
    except ValueError:
      print("Invalid port number. Please enter an integer.")

  # Perform banner grabbing with different tools
  for tool in ["netcat", "telnet", "nmap"]:
    banner = banner_grab(target, port, tool)
    print(banner)

if __name__ == "__main__":
  main()
