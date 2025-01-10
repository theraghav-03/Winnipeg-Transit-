# Name : Raghav sharma
# date : 09/01/2025
# Description : Using Winnipeg Transit API to get the nearby stops and their schedules

import json
import turtle
import urllib.request
from colorama import Fore, Back, Style

API_KEY = 'GpySP2xycRk1KCahLdcT'
 
lon = -97.197585 # GPS longitude of 45 smithurst street
lat = 49.936993  # GPS latitude of 45 smithurst street
distance = 500  # radius in meters to search around GPS coordinates

 # url to request stops
url_stops = f"https://api.winnipegtransit.com/v3/stops.json?lon={lon}&lat={lat}&distance={distance}&api-key={API_KEY}"
 
 
response = urllib.request.urlopen(url_stops)
stops = json.loads(response.read())

# print(stops)

print("Nearby stops within 500m:")
for stop in stops['stops']:
    print(f"Stop Number: {stop['key']} -> \n  Stop Name: {stop['name']} - {stop['distances']['direct']} meters away on {stop['street']['name']} \n")

