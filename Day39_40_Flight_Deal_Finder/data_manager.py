import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv("Day39_40_Flight_Deal_Finder/.env")
sheety_bearer_token = os.getenv("BEARER_TOKEN")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_header={
            "Authorization": f"Bearer {sheety_bearer_token}" 
        }
        self.dest_sheet_data={}
        self.customer_data={}
        
    def getData(self):
        response=requests.get(url="https://api.sheety.co/6e94b3d5304ddf6d53ea8022eb513017/flightDealsPythonDay39/prices",headers=self.sheety_header)
        data=response.json()
        print(f"data from sheety: {data}")
        self.dest_sheet_data=data["prices"]
        return self.dest_sheet_data
    
    def updateCodes(self):
        for city in self.dest_sheet_data:
            new_data={
                "price":{
                    "iataCode":city["iataCode"]
                }
                
            }
            response=requests.put(url=f"https://api.sheety.co/6e94b3d5304ddf6d53ea8022eb513017/flightDealsPythonDay39/prices/{city['id']}",json=new_data,headers=self.sheety_header)
            print(response.text)
            
    def get_customer_emails(self):
        response=requests.get(url="https://api.sheety.co/6e94b3d5304ddf6d53ea8022eb513017/flightDealsPythonDay39/users")
        self.customer_data=response.json()["users"]
        return self.customer_data
        