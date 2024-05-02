#!/usr/bin/env python3
    
# Script Name:                                  Uptime Sensor Tool part 2
# Author:                                       Cody Blahnik
# Date of latest revision:                      05/01/2024
# Purpose:                                      sendneamails to users.

import smtplib  # Importing smtplib library for handling SMTP protocol
from email.mime.text import MIMEText  # Importing MIMEText class to construct text emails
from email.mime.multipart import MIMEMultipart  # Importing MIMEMultipart class to construct multipart emails
import datetime  # Importing datetime module to work with dates and times

def main():
    # Prompting the user to enter their email address and password separated by space
    user_email, password = input("Enter your email address and password separated by space: ").split()
    host, previous_status, current_status = "whomever", "down", "up"  # Example values for host and status
    send_email(user_email, password, host, previous_status, current_status)  # Calling the send_email function

def send_email(user_email, password, host, previous_status, current_status):
    admin_email = "admin@example.com"  # Administrator's email address
    subject = f"Status Change Notification for {host}"  # Email subject indicating the status change
    # Constructing the email body with information about the status change
    message = f"Host {host} status changed from {previous_status} to {current_status} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."

    msg = MIMEMultipart()  # Creating a multipart message
    msg.attach(MIMEText(message, 'plain'))  # Attaching the message body to the email
    msg['From'] = user_email  # Setting the sender's email address
    msg['To'] = admin_email  # Setting the recipient's email address
    msg['Subject'] = subject  # Setting the subject of the email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Connecting to Gmail's SMTP server
        server.starttls()  # Starting TLS encryption
        server.login(user_email, password)  # Logging in to the SMTP server with user's credentials
        server.sendmail(user_email, admin_email, msg.as_string())  # Sending the email
        # The 'with' statement ensures that the SMTP connection is automatically closed after sending the email

    print("Email sent successfully!")  # Printing a success message after sending the email


main()  # Executing the main function to start the program
