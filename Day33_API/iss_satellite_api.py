import requests
import datetime as dt
import smtplib
import time

# email details:
from dotenv import load_dotenv
import os
load_dotenv("Day33_API/.env")
# smtp credentials:
my_email="apathak1_be22@thapar.edu"
password=os.getenv("EMAIL_PASSWORD")
print(f"Password fetched by env is: {password}")

MY_LATITUDE=30.733315
MY_LONGITUDE=76.779419

def iss_is_overhead():
    # getting sunrise & sunset:
    # get iss longitude & latitude:
    response=requests.get(url="http://api.open-notify.org/iss-now.json") 
    data=response.json()
    # print(data)
    iss_longitude=float(data["iss_position"]["longitude"])      #typecast from string to float
    iss_latitude=float(data["iss_position"]["latitude"])       #typecast from string to float

    if MY_LONGITUDE-5<iss_longitude<MY_LONGITUDE+5 and MY_LATITUDE-5<iss_latitude<MY_LATITUDE+5 :
        return True
    
def is_night_time():
    parameters={
        "lat":MY_LATITUDE,
        "lng":MY_LONGITUDE,    
        "formatted":0,      #so that we get in 24hour format
    }       #as dictionary 

    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()

    data=response.json()

    sunrise_time=data["results"]["sunrise"]
    sunrise_hour=sunrise_time.split('T')[1].split(':')[0]

    sunset_time=data["results"]["sunset"]
    sunset_hour=sunset_time.split('T')[1].split(':')[0]

    times=(sunrise_hour,sunset_hour)      #both as string
    sunrise_hour=int(sunrise_hour)
    sunset_hour=int(sunset_hour)

    print(f"Tuple of extracted sunrise & sunset hour: {times}")

    current_time=dt.datetime.now()
    current_time=current_time.time()
    # print(current_time)
    # split to get only hour
    current_hour=str(current_time).split(':')[0]
    print(f"Current extracted hour: {current_hour}")     #string
    current_hour=int(current_hour)
    
    if current_hour>=sunset_hour or current_hour<=sunrise_hour:
        return True
        
while True:
    # to execute this code every 60 seconds:
    time.sleep(60)
    # check if it is currently dark & iss is at my location with a buffer of 5:
    if iss_is_overhead() and is_night_time():
        # send me email to look up
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()       #for secure
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="pathakshita07@gmail.com",
                msg=f"Subject:ISS overhead!!\n\nLook up! There is an ISS overhead"
            )
