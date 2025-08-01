import requests
import json
import os #Import os to secure our APIKEY as env variable

class RandomNumberGenerator:
    def __init__(self):
        self.API_KEY = os.environ.get("RANDOM_NUM_API_KEY") 
        self.url = "https://api.random.org/json-rpc/4/invoke"

        if not self.API_KEY:
            print("API KEY had not been set in the OS")
            


    def generate_random_integers(self):
        payload = {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params" : {
                "apiKey": self.API_KEY,
                "n": 4,
                "min": 0,
                "max": 7,
                "base": 10,
                "replacement": True,
            },
            "id":1
        }
        try:
            response = requests.post(self.url,json=payload)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            response_json = response.json()

            # print(response_json)
            if "result" in response_json:
                random_data = response_json["result"]["random"]["data"]
                return random_data
            else:
                print("Error: 'result' key not found in the response.")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Error calling random.org API: {e}")
            return None # Return None to indicate an error
