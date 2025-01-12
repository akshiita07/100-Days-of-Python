# AUTOMATIC BIRTHDAY MAIL SENDER PROJECT:
import smtplib
import datetime as dt
import random
import pandas

# fetch csv file:
data=pandas.read_csv("Day32_Email_SMTP_DateTime_Modules/Automated_Birthday_Wisher_Project/birthdays.csv")
# convert data to a dictionary: format birthdays_dict = {  (month, day): data_row  }
data_dict={(data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()}
print(data_dict)

# fetching date:
current=dt.datetime.now()

# Check if today matches a birthday in the birthdays.csv
day=current.day
month=current.month
today=(month,day)        #todays tuple
print(today) 

# FOR .env file: pip install python-dotenv
from dotenv import load_dotenv
import os
load_dotenv("Day32_Email_SMTP_DateTime_Modules/.env")
# smtp credentials:
my_email="apathak1_be22@thapar.edu"
password=os.getenv("EMAIL_PASSWORD")
# print(f"Password fetched by env is: {password}")

if today in data_dict:
    print("Birthday today")
    # pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    random_number=random.randint(1,3)
    with open(f"Day32_Email_SMTP_DateTime_Modules/Automated_Birthday_Wisher_Project/letter_templates/letter_{random_number}.txt") as letter:
        contents=letter.read()
        contents=contents.replace("[NAME]", data_dict[today]["name"])       #for replace to work we must add = here
        # send mail to that persons email id
        # Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()       #for secure
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=data_dict[today]["email"],
                msg=f"Subject:Happy Birthday from Python:)\n\n{contents}"
            )