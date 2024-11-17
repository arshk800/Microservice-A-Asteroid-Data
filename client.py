import requests
import json

start_date = input("Enter a start date (YYYY-MM-DD):")
end_date = input("Enter an end date (YYYY-MM-DD):")

port = 8000
# request url with query parameters
url = f"http://localhost:{port}/asteroids?start_date={start_date}&end_date={end_date}"

message = requests.get(url)

status_code = message.status_code
if status_code == 200:
    print("Request successful!")
    # pretty-print json
    print(json.dumps(message.json(), indent=4))
else:
    print("Status Code:", message.status_code)
    try:
        error = message.json()
        print(f"Error: {error.get('Error', 'Try again!')}")
    except ValueError: # print error in case of other problems
        print("Unable to fetch data")



