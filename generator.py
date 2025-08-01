import requests
import json

API_KEY = "YOUR API KEY"
url = "https://api.random.org/json-rpc/4/invoke"


def generate_random_integers():
    payload = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params" : {
            "apiKey": API_KEY,
            "n": 4,
            "min": 0,
            "max": 7,
            "base": 10,
            "replacement": True,
        },
        "id":1
    }
    try:
        response = requests.post(url,json=payload)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        response_json = response.json()

        # print(response_json)
        if "result" in response_json:
            random_data = response_json["result"]["random"]["data"]
            return random_data
        else:
            print("Error: 'result' key not found in the response.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error calling random.org API: {e}")
        return None # Return None to indicate an error
