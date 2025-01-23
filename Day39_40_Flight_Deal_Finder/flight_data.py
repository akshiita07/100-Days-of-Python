import os
import requests
from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime,timedelta

load_dotenv("Day39_40_Flight_Deal_Finder/.env")

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,origin_airport,dest_airport,depart_date,return_date,stops):
        self.price=price
        self.origin_airport=origin_airport
        self.dest_airport=dest_airport
        self.depart_date=depart_date
        self.stops=stops
            
    def updateIATA_code(self,city_name):
        from flight_search import FlightSearch
        flightSearch=FlightSearch()
        code=flightSearch.get_iata_code(city_name)
        return code
    
    def find_cheapest_flight(data):

        if data is None or not data["data"]:
            print("No flight data")        
            return FlightData("N/A","N/A","N/A","N/A","N/A") #init fnc
        
        flight=data["data"][0]
        lowest_price=float(flight["price"]["grandTotal"])
        no_of_stops=len(flight["itineraries"][0]["segments"])-1
        origin_airport=flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        dest_airport=flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        depart_date=flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        return_date=flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
        
        cheapest_flight=FlightData(lowest_price,origin_airport,dest_airport,depart_date,return_date)
        
        for flight in data["data"]:
            price=float(flight["price"]["grandTotal"])
            
            if price<lowest_price:
                lowest_price=price
                origin_airport=flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                dest_airport=flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                depart_date=flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                return_date=flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                
                cheapest_flight=FlightData(lowest_price,origin_airport,dest_airport,depart_date,return_date)
                print(f"Lowest price to {dest_airport} is ₹{lowest_price}")

        return cheapest_flight
