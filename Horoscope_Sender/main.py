import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv("Horoscope_Sender/.env")

# from twilio:
account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOKEN")

print(f"AUTH_TOKEN: {auth_token}")
print(f"AUTH_SID: {account_sid}")

#Rapid api:
url = "https://astropredict-daily-horoscopes-lucky-insights.p.rapidapi.com/horoscope"

parameters = {"lang":"en","zodiac":"pisces","type":"daily"}

headers = {
	"x-rapidapi-key": "b600b333edmsh95738b0822961cfp1ccb67jsnb7258f166b5e",
	"x-rapidapi-host": "astropredict-daily-horoscopes-lucky-insights.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=parameters)

# print(response.json())
content=response.json()
# print(content["horoscope"])
horoscope_content=content["horoscope"]

# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def sendMessage():
    client = Client(account_sid, auth_token)
    
    # send WHATSAPP TEXT:
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"Good Morning Aki\nLets get it today💪🏻\n\nHere is your horoscope:\n{horoscope_content}\n\nDrink Water\nExercise\nLESSGOOO GRAB THE DAYY",
            to='whatsapp:+918283840233'       
        )    
        print(f"Message sent successfully. SID: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")
        
sendMessage()