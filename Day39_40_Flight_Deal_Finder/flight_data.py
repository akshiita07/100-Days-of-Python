import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv("Day39_40_Flight_Deal_Finder/.env")

class FlightData:
    #This class is responsible for structuring the flight data.
            
    def updateIATA_code(self,city_name):
        from flight_search import FlightSearch
        flightSearch=FlightSearch()
        code=flightSearch.get_iata_code(city_name)
        return code
