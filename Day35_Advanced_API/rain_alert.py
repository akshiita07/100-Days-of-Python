#API Key: To track how much API content we r using & to authorize & deny access if gone over the limit

import requests
# pip install twilio
from twilio.rest import Client
# for environment variables:
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv("Day35_Advanced_API/.env")
# print(f"Env File Found: {find_dotenv()}")

# from twilio:
account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOKEN")

# https://home.openweathermap.org/api_keys
apiKey=os.getenv("API_KEY")

# print(f"API_KEY: {apiKey}")
# print(f"AUTH_TOKEN: {auth_token}")
# print(f"AUTH_SID: {account_sid}")

MY_LATITUDE=30.339781
MY_LONGITUDE=76.386879

parameters={
    "lat":MY_LATITUDE,
    "lon":MY_LONGITUDE,
    "appid":apiKey,
    "cnt":4,
}

response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
# print(f"Status code is: {response.status_code}")
response.raise_for_status()
weather_data=response.json()
# print(weather_data)
# json viewer: https://jsonviewer.stack.hu/

will_rain=False
for i in range(0,4):
    # print(weather_data["list"][i]["weather"][0]["id"])
    if int(weather_data["list"][i]["weather"][0]["id"])<700:
        will_rain=True
        
if will_rain:
    # print("Bring an umbrella")
    client = Client(account_sid, auth_token)
    
    # send SMS:
    '''
    message = client.messages.create(
        body="It's going to rain today so carry an umbrella!☔",
        from_="+16204079926",       #from twilio
        to="+918283840233",         #to send msg to ourself
    )

    print(message.status)
    print(message.body)
    '''
    
    # send WHATSAPP TEXT:
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today so carry an umbrella!☔",
        to='whatsapp:+918283840233'
        
    )

    print(message.sid)