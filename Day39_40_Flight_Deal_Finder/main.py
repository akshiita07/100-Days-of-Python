# libraries import:
import requests
import os
from twilio.rest import Client
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

# Check if IATA code corresponding is not filled then fill it:
for row in sheet_data:
    search_flight=FlightData()
    if row["iataCode"]=="":
        row["iataCode"]=search_flight.updateIATA_code(row["city"])

    data_manager.dest_sheet_data=sheet_data
    data_manager.updateCodes()
    
