# smtplib library to send emails
# Gmail: smtp.gmail.com     SIMPLE MAIL TRANFER PROTOCOL
# Python mail app: password-uedr ftsu yiok uoji
# ADDING PORT NUMEBR: smtplib.SMTP("smtp.gmail.com", port=587)
import smtplib

# FOR .env file: pip install python-dotenv
from dotenv import load_dotenv, find_dotenv
import os
# dotenv_path = find_dotenv()
# print(f".env file found at: {dotenv_path}")  # Check if the .env file is detected

load_dotenv("Day32_Email_SMTP_DateTime_Modules/.env")

my_email="apathak1_be22@thapar.edu"
password=os.getenv("EMAIL_PASSWORD")
print(f"Password fetched by env is: {password}")

# using close():
"""
connection=smtplib.SMTP("smtp.gmail.com")       #to connect to ur gmail
connection.starttls()       #TLS: TRANSPORT LAYER SECURITY: to secure our connection to email server
connection.login(user=my_email,password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="pathakshita07@gmail.com",
    msg="Subject:From Python\n\nHi Akshita from python smtp")
connection.close()
"""

# without using close():
with smtplib.SMTP("smtp.gmail.com") as connection:       #to connect to ur gmail
    connection.starttls()       #TLS: TRANSPORT LAYER SECURITY: to secure our connection to email server
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="pathakshita07@gmail.com",
        msg="Subject:From Python\n\nHi Akshita from python smtp")