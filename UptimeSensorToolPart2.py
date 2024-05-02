#!/usr/bin/env python3
    
# Script Name:                                  Uptime Sensor Tool part 2
# Author:                                       Cody Blahnik
# Date of latest revision:                      05/01/2024
# Purpose:                                      sendneamails to users.

import smtplib  # importing smtplib library for handling SMTP protocol
from email.mime.text import MIMEText  # importing MIMEText class to construct text emails
from email.mime.multipart import MIMEMultipart  # importing MIMEMultipart class to construct multipart emails
import datetime  # importing datetime module to work with dates and times

def send_email(user_email, password, host, previous_status, current_status):
    admin_email = "admin@example.com"  # administrator's email address
    subject = f"Status Change Notification for {host}"  # email subject indicating the status change
    message = f"Host {host} status changed from {previous_status} to {current_status} on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."  # email body with information about the status change
    
    msg = MIMEMultipart()  # creating a multipart message
    msg['From'] = user_email  # setting the sender's email address
    msg['To'] = admin_email  # setting the recipient's email address
    msg['Subject'] = subject  # setting the subject of the email
    body = MIMEText(message, 'plain')  # creating a MIMEText object with the message body
    msg.attach(body)  # attaching the message body to the email
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:  # connecting to Gmail's SMTP server
        server.starttls()  # starting TLS encryption
        server.login(user_email, password)  # logging in to the SMTP server with user's credentials
        server.sendmail(user_email, admin_email, msg.as_string())  # sending the email
        # the 'with' statement ensures that the SMTP connection is automatically closed after sending the email
    
    print("Email sent successfully!")  # printing a success message after sending the email

def main():
    user_email = input("Enter your email address: ")  # prompting the user to enter their email address
    password = input("Enter your password: ")  # prompting the user to enter their email password
    
    host = "ExampleHost"  # the host whose status changed (example value)
    previous_status = "down"  # previous status of the host (example value)
    current_status = "up"  # xurrent status of the host (example value)
    
    send_email(user_email, password, host, previous_status, current_status)  # calling the send_email function

if __name__ == "__main__":
    main()  # calling the main function when the script is executed directly
