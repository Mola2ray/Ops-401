#!/usr/bin/python3
# Lamin Touray
# Scripts: Add a log rotation feature based on size



import logging
import subprocess
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from logging.handlers import RotatingFileHandler

# Set up a specific logger with our desired output level
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

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

# Source: chaGPT       
