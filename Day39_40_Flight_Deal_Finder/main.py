# libraries import:
import requests
import os
from datetime import datetime,timedelta
from dotenv import load_dotenv
load_dotenv("Day39_40_Flight_Deal_Finder/.env")
# pretty print library to view json in formatted way:
from pprint import pprint

# classes import:
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# get env file keys:
amadeus_api_key = os.getenv("API_KEY")
amadeus_api_secret = os.getenv("API_SECRET")
twilio_acc_sid = os.getenv("ACCOUNT_SID")
twilio_auth_token = os.getenv("AUTH_TOKEN")
sheety_bearer_token = os.getenv("BEARER_TOKEN")

# CHECK IF ENV KEYS WORKING:
# print(f"Amadeus api key: {amadeus_api_key}")
# print(f"Amadeus api secret: {amadeus_api_secret}")

# SHEETY API: https://dashboard.sheety.co/projects/678dbfa47c36d479f76cba63/sheets/prices


# Get data from google sheets:
data_manager=DataManager()
sheet_data=data_manager.getData()
# pprint(sheet_data)

# user emails:
user_emails=data_manager.get_customer_emails()
pprint(user_emails)

customer_emails=[row["email"] for row in user_emails]

# Check if IATA code corresponding is not filled then fill it:
for row in sheet_data:
    search_flight=FlightData()
    
    # if iatacodes are NOT pre-filled:
    if row["iataCode"]=="":
        row["iataCode"]=search_flight.updateIATA_code(row["city"])  #corresponding city name from google sheets ka IATA code retrieve
    data_manager.dest_sheet_data=sheet_data
    data_manager.updateCodes()
    
    search_flight.find_cheapest_flight(row["iataCode"])

# SEARCH FOR FLIGHTS:
today=datetime.now()
print(f"Today is: {today}")
tmrw=datetime.now()+timedelta(days=1)
print(f"Tommorrow is: {tmrw}")
after6Months=today+timedelta(days=180)
print(f"Date after 6 months is: {after6Months}")

for dest in sheet_data:
    print(f"Search flight for {dest['city']}:")
    flight_search=FlightSearch()
    flights=flight_search.check_flights("LON",dest["iataCode"],tmrw,after6Months)

    flight_data=FlightData()
    cheapestFlight=flight_data.find_cheapest_flight(flights)
    
    print(f"{dest['city']} : ₹{cheapestFlight.price}")

    if cheapestFlight.price=="N/A":
        print(f"No direct flights found for {dest['city']}. Looking for indirect flights")
        
        flights=flight_search.check_flights("LON",dest["iataCode"],tmrw,after6Months,False)
        
        cheapestFlight=flight_data.find_cheapest_flight(flights)
        print(f"Cheapest indirect flight {dest['city']} : ₹{cheapestFlight.price}")
        
    if cheapestFlight.price!="N/A" and cheapestFlight.price<dest["lowestPrice"]:
        
        if cheapestFlight.no_of_stops==0:
            message=f"Low Price Alert!\nOnly ₹{cheapestFlight.price} to fly DIRECTLY from {cheapestFlight.origin_airport} to {cheapestFlight.dest_airport}, on {cheapestFlight.depart_date} until {cheapestFlight.return_date}\n"
        else:
            message=f"Low Price Alert!\nOnly ₹{cheapestFlight.price} to fly DIRECTLY from {cheapestFlight.origin_airport} to {cheapestFlight.dest_airport}, with {cheapestFlight.no_of_stops} stop(s), on {cheapestFlight.depart_date} until {cheapestFlight.return_date}\n"
        
        notif_manager=NotificationManager()
        notif_manager.send_whatsapp(message)
        notif_manager.send_email(user_emails,message)
        


