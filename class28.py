#!/usr/bin/python3
# Lamin Touray
# Scripts:Use StreamHandler and FileHandler in your Python script.
# FileHandler should write to a local file.
# StreamHandler should output to the terminal.


import logging
import subprocess
import time
import datetime
import smtplib
from email.mime.text import MIMEText

# Set up a specific logger with our desired output level
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)

# Create a file handler
file_handler = logging.FileHandler('app.log')

# Create a stream handler
stream_handler = logging.StreamHandler()

# Set a format for both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def send_email(sender_email, sender_password, recipient_email, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            logger.info("Email sent successfully.")
    except Exception as e:
        logger.error("Error sending email: %s", e)


sender_email = input("Enter the sender email address: ")
sender_password = input("Enter the sender email password: ")
recipient_email = input("Enter the recipient email address: ")

ip = "10.0.0.253"

interval = 2

previous_status = None

while True:
    try:
        ping = subprocess.Popen(
            ["ping", "-c", "1", "-W", "1", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, error = ping.communicate()

        if "1 received" in out.decode("utf-8"):
            status = "Network Active"
        else:
            status = "Network Inactive"

        if previous_status is not None and status != previous_status:
            timestamp = datetime.datetime.now()
            subject = f"Host Status Change: {ip}"
            body = f"The status of host {ip} has changed from {previous_status} to {status} at {timestamp}."
            send_email(sender_email, sender_password, recipient_email, subject, body)

        logger.info("%s %s to %s", datetime.datetime.now(), status, ip)

        previous_status = status
        time.sleep(interval)
    except Exception as e:
        logger.error("Error in main loop: %s", e)


