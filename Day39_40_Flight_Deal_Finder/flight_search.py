import requests
import os
from dotenv import load_dotenv
load_dotenv("Day39_40_Flight_Deal_Finder/.env")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.amadeus_api_key = os.getenv("API_KEY")
        self.amadeus_api_secret = os.getenv("API_SECRET")
        self.access_token=self.get_new_token()
        
    def get_new_token(self):
        # get your access token based on your API Key and API Secret
        access_token_header={
            "Content-Type":"application/x-www-form-urlencoded"
        }
        access_token_data={
            "grant_type":"client_credentials",
            "client_id":self.amadeus_api_key,
            "client_secret":self.amadeus_api_secret,
        }
        response=requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token",data=access_token_data,headers=access_token_header)
        self.access_token=response.json()["access_token"]
        print(f"Access token printing inside flight_search: {self.access_token}")
        print(f"Your access token expires in: {response.json()["expires_in"]} seconds")
        return self.access_token
    
    def get_iata_code(self,city_name):
        parameters={
            "keyword":city_name,
            "max":2,
            "include":"AIRPORTS",
        }
        header = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response=requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities",params=parameters,headers=header)
        
        try:
            code=response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code
    
    def check_flights(self,origin_airport,dest_airport,depart_date,return_date,is_direct=True):
        
        header = {
            "Authorization": f"Bearer {self.access_token}"
        }
        parameters={
            "originLocationCode":origin_airport,
            "destinationLocationCode":dest_airport,
            "departureDate":depart_date.strftime("%Y-%m-%d"),   #tommorrow & 6months (6*30=180 days time) YYYY-MM-DD format
            "returnDate":return_date.strftime("%Y-%m-%d"),
            "adults":1,
            "nonStop":True if is_direct else False,
            "max":10,
            "currencyCode":"INR",
        }

        response=requests.get(url="test.api.amadeus.com/v2/shopping/flight-offers",params=parameters,headers=header)

        response.raise_for_status()
        print(f"Search flight price status code: {response.status_code()}")
        print(f"Search flight price: {response.json()}")
        
        # error handling when response code is not 200:
        
        return response.json()