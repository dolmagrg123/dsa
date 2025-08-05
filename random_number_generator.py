from internal_generator import InternalGenerator
import requests
import json
import datetime
#Import os to secure our APIKEY as env variable
# import os 

class RandomNumberGenerator:
    def __init__(self, num, min, max):
        self.url = "https://www.random.org/integers/"
        self.num = num
        self.min = min
        self.max = max
        self.internal_num = InternalGenerator(self.num, self.min, self.max)
        
#parmas under init???
    def generate_random_integers(self):
        params = {
            "num": self.num,        # Number of integers requested
            "min": self.min,        # The smallest value returned
            "max": self.max,        # The largest value returned
            "col": 1,        # Number of columns used to display the returned values
            "base": 10,      # Use base 10 system
            "format": "plain",  # Returns response in a plain text
            "rnd": "new"     # Generate a new random numbers
        }
        try:
            response = requests.get(self.url,params=params)

            if response.status_code == 200:
                numbers = response.text.strip().split('\n') # .strip() to remove any whitespace, .split('\n') create a list 
                random_data = [int(num) for num in numbers] #converts the list of string into integers
                return random_data
            else:
                with open("error.log", "a") as f: #append error into error.log
                    f.write(f"\n API_URL ERROR: Date and Time: {datetime.datetime.now()} \n Error Code: {response.status_code}")
                
                #return list of random generated number without using API
                return (self.internal_num.internal_number())
                
        except requests.exceptions.RequestException as e:
            print(f"Error calling random.org API: {e}")
            return None # Return None to indicate an error
