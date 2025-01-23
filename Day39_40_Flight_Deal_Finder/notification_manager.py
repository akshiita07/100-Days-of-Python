import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv("Day39_40_Flight_Deal_Finder/.env")
twilio_acc_sid = os.getenv("ACCOUNT_SID")
twilio_auth_token = os.getenv("AUTH_TOKEN")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(twilio_acc_sid, twilio_auth_token)

    def send_whatsapp(self,msgBody):
        # send WHATSAPP TEXT:
        message = self.client.messages.create(
            from_='whatsapp:+14155238886',
            body=msgBody,
            to='whatsapp:+918283840233'       
        )

    def send_email(self,email_list,msgBody):
        import smtplib
        my_email = os.getenv("MY_EMAIL")
        password = os.getenv("EMAIL_PASSWORD")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()       #for secure
            connection.login(user=my_email,password=password)
            for email in email_list:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:Flight Tickets!!\n\n{msgBody}".encode('utf-8')
                )
