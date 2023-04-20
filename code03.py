#!/usr/bin/python3
# Lamin Touray



import subprocess
import time
import datetime
import smtplib
from email.mime.text import MIMEText

# Function to send email notifications
def send_email(sender_email, sender_password, recipient_email, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", e)


# Ask for the email address and password for sending notifications
sender_email = input("Enter the sender email address: ")
sender_password = input("Enter the sender email password: ")
recipient_email = input("Enter the recipient email address: ")

# Define the IP address to ping
ip = "10.0.0.253"

# Define the interval between pings (in seconds)
interval = 2

# Initialize previous status
previous_status = None

# Main loop
while True:
    # Ping the IP address
    ping = subprocess.Popen(
        ["ping", "-c", "1", "-W", "1", ip],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, error = ping.communicate()

    # Evaluate the response
    if "1 received" in out.decode("utf-8"):
        status = "Network Active"
    else:
        status = "Network Inactive"

    # If the status has changed, send an email
    if previous_status is not None and status != previous_status:
        timestamp = datetime.datetime.now()
        subject = f"Host Status Change: {ip}"
        body = f"The status of host {ip} has changed from {previous_status} to {status} at {timestamp}."
        send_email(sender_email, sender_password, recipient_email, subject, body)

    # Print the result with a timestamp
    print(
        f"{datetime.datetime.now()} {status} to {ip}"
    )

    # Update previous status and wait for the specified interval
    previous_status = status
    time.sleep(interval)


# Source: chatGPT

# Sources: chatGPT


