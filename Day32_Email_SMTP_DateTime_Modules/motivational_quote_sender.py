# if it is a particular date & time then email ourself a motivational quote
import smtplib
import datetime as dt
import random

# fetching day:
current=dt.datetime.now()
current_day=current.weekday()
# print(current_day)


# FOR .env file: pip install python-dotenv
from dotenv import load_dotenv
import os
load_dotenv("Day32_Email_SMTP_DateTime_Modules/.env")
# smtp credentials:
my_email="apathak1_be22@thapar.edu"
password=os.getenv("EMAIL_PASSWORD")
print(f"Password fetched by env is: {password}")
    
# on a monday:
if(current_day==1):
    # select random quote from list of quotes
    with open("Day32_Email_SMTP_DateTime_Modules/quotes.txt") as quotes_file:
        quotes_list=quotes_file.readlines()
        random_quote=random.choice(quotes_list)
    # print(random_quote) 
    
    # send mail
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()       #for secure
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pathakshita07@gmail.com",
            msg=f"Subject:You got this Akshu!\n\n{random_quote}"
        )