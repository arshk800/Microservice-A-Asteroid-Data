import json
import random
import requests
from flask import Flask, jsonify, request


app = Flask(__name__)
port = 8000

@app.route('/asteroids', methods=['GET'])
def get():
    # Get the start and end dates from the client
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date', start_date)  # default to start date if end_date is not given

    # NASA API with given queries
    response = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key=DEMO_KEY")

    if response.status_code != 200:
        return jsonify({"Error": "Unable to fetch data! Please check date format or enter appropriate date and try again."}), 500

    data = response.json()
    asteroid_dict = {'date': start_date}
    near_earth_objects = data.get('near_earth_objects', {}).get(f'{start_date}', [])

    asteroid_icons = [
        "https://www.flaticon.com/free-icon/asteroid_7480279",
        "https://www.flaticon.com/free-icon/asteroids_8572599",
        "https://www.flaticon.com/free-icon/asteroid_2530826",
        "https://www.flaticon.com/free-icon/asteroid_9407479",
        "https://www.flaticon.com/free-icon/astronomy_16115859",
        "https://www.flaticon.com/free-icon/asteroid_3601495"
    ]

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
            'icon_url': random.choice(asteroid_icons)
        }
        for asteroid in near_earth_objects
    ]

    pretty_print = json.dumps(asteroid_dict, indent=4)
    return app.response_class(
        pretty_print, mimetype='data/json') # 'mimetype' = JSON data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

