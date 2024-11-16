import json
import requests
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP) # socket type REP
socket.bind("tcp://*:5555")

#  Wait for message from client.py
message = socket.recv()

# decode code from byte to regular string
message = message.decode('utf-8')
print(f"Asteroid data for date: {message}")

time.sleep(1)

start_date = message.strip()
end_date = start_date    # YYYY-MM-DD
response = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key=DEMO_KEY")

# json response with all the asteroid info
data = response.json()

asteroid_list = []
asteroid_dict = {'date': start_date}
near_earth_objects = data.get('near_earth_objects', {}).get(f'{start_date}', [])

asteroid_icons = [
    "https://www.pngegg.com/en/png-eitrv"
    "https://www.pngegg.com/en/png-eitrv"
    "https://www.pngegg.com/en/png-eitrv"
    "https://www.pngegg.com/en/png-eitrv"
    "https://www.pngegg.com/en/png-eitrv"
]

# using list comprehension
asteroid_dict['asteroids'] = [
    {
        'name': asteroid.get('name', 'N/A'),
        'estimated_diameter': estimated_diameter.get('kilometers', {}) if (estimated_diameter := asteroid.get('estimated_diameter', {})) else {},
        'is_potentially_hazardous': asteroid.get('is_potentially_hazardous_asteroid'),
        'close_approach_data': {
            'close_approach_date': close_approach_data[0].get('close_approach_date', 'N/A') if (close_approach_data := asteroid.get('close_approach_data', [])) else '',
            'relative_velocity':
                {"kilometers_per_hours": close_approach_data[0].get('relative_velocity', {}).get('kilometers_per_hour') if close_approach_data else ''
                 },
            'miss_distance': {
                'kilometers': close_approach_data[0].get('miss_distance', {}).get('kilometers') if close_approach_data else ''
            }
        },
    'icon_url':""
    }
    for asteroid in near_earth_objects
]

# impose pretty-print json
pretty_print = json.dumps(asteroid_dict, indent=4)
socket.send_string(pretty_print)


