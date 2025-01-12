# Name : Raghav sharma
# date : 09/01/2025
# Description : Using Winnipeg Transit API to get the nearby stops and their schedules

import json
import turtle
import urllib.request
from dateutil.parser import parse
from datetime import datetime
from colorama import Fore, Back, Style

API_KEY = 'GpySP2xycRk1KCahLdcT'
 
lon = -97.197585 # GPS longitude of 45 smithurst street
lat = 49.936993  # GPS latitude of 45 smithurst street
distance = 300  # radius in meters to search around GPS coordinates

 # url to request stops
url_stops = f"https://api.winnipegtransit.com/v3/stops.json?lon={lon}&lat={lat}&distance={distance}&api-key={API_KEY}"
 
 
response = urllib.request.urlopen(url_stops)
stops = json.loads(response.read())

# print(stops)

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"Nearby stops within {distance}m:")
for stop in stops['stops']:
    print(f"Stop Number: {stop['key']} -> \n  Stop Name: {stop['name']} - {stop['distances']['direct']} meters away on {stop['street']['name']} \n")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")


#stops dictionary
stops_dict = {stop['key']: stop['name'] for stop in stops['stops']}
# print(stops_dict)

stop_number = int(input("Enter a stop number to get the schedule:\n "))

if stop_number in stops_dict:
    stop_info = stops_dict[stop_number]
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-")
    print("Schedule for stop:",stop_number,"-",stop_info,":::")

    #url for bus schedules
    url_schedule = f"https://api.winnipegtransit.com/v3/stops/{stop_number}/schedule.json?max-results-per-route=3&api-key={API_KEY}"
    responses = urllib.request.urlopen(url_schedule)
    schedules = json.loads(responses.read())
    # print(schedules)
    # bus_number_dict = {schedule['route']['number']: schedule['route']['name'] for schedule in schedules['stop-schedule']['route-schedules']}
    # print(bus_number_dict)
    
    print(f"Bus number     \t\tBus Name    \t\t\tArrival Time   \t\tEstimated Time")
    for schedule in schedules['stop-schedule']['route-schedules'] :
        bus_name = schedule['route']['name']
        bus_number = schedule['route']['number']
        
        for bus in schedule['scheduled-stops']:
            arrival_time = parse(bus['times']['arrival']['scheduled'])
            estimated_time = parse(bus['times']['arrival']['estimated'])
            
            if estimated_time > arrival_time:
                print(f" {bus_number} \t\t{bus_name}  \t\t {Fore.RED}{arrival_time.strftime("%I:%M %p")} \t\t {estimated_time.strftime("%I:%M %p")}\t LATE{Fore.RESET}")
            elif estimated_time < arrival_time:
                print(f" {bus_number} \t\t{bus_name}  \t\t {Fore.BLUE}{arrival_time.strftime("%I:%M %p")} \t\t {estimated_time.strftime("%I:%M %p")}\t EARLY{Fore.RESET}")
            else:
                print(f" {bus_number} \t\t{bus_name}  \t\t {Fore.GREEN}{arrival_time.strftime("%I:%M %p")} \t\t {estimated_time.strftime("%I:%M %p")}\t OK{Fore.RESET}")    
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-")
else:
    print("Invalid stop number")
    
    
    
    
    
    
#     for schedule in schedules['stop-schedule']['route-schedules']:
#         print(f"{schedule['route']['number']}  \t\t{schedule['route']['name']} \t\t\t{schedule['scheduled-stops'][0]['times']['departure']['scheduled']}")
#     print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-")
# else :
#     print("Invalid stop number")        






# print(Fore.RED + 'some red text')
# print(Back.CYAN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')