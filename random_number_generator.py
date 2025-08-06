"""
Author: DG
Version: 2.0
Date: August 2025
Purpose: External random number generation using random.org API.
         Fetches truly random numbers for target combinations with
         fallback to internal generation on API failure.
"""

from internal_generator import InternalGenerator
import requests
import datetime

class RandomNumberGenerator:
    def __init__(self, length, min_val, max_val):
        self.url = "https://www.random.org/integers/"
        self.length = length
        self.min_val = min_val
        self.max_val = max_val
        self.internal_generator = InternalGenerator(self.length, self.min_val, self.max_val)

    def generate_random_integers(self):
        params = {
            "num": self.length,        # Number of integers requested
            "min": self.min_val,        # The smallest value returned
            "max": self.max_val,        # The largest value returned
            "col": 1,        # Number of columns used to display the returned values
            "base": 10,      # Use base 10 system
            "format": "plain",  # Returns response in a plain text
            "rnd": "new"     # Generate a new random numbers
        }
        try:
            response = requests.get(self.url,params=params)

            if response.status_code == 200:
                # cleanup the response and split with new line
                numbers = response.text.strip().split('\n') 

                generated_numbers = []
                for num in numbers:
                    num = num.strip()
                    if num.isdigit():
                        generated_numbers.append(int(num))
                if generated_numbers:
                    # print(random_data)
                    return generated_numbers
                else:
                    with open("error.log", "a") as f:
                        f.write(f"\n Date and Time: {datetime.datetime.now()} \n No valid numbers found in server response.")
                    return (self.internal_generator.internal_number())
                
            else:
                with open("error.log", "a") as f:
                    f.write(f"\n API_URL ERROR: Date and Time: {datetime.datetime.now()} \n Error Code: {response.status_code}")

                #return list of random generated number without using API
                return (self.internal_generator.internal_number())
                
        except requests.exceptions.RequestException as e:
            print(f"Error calling random.org API: {e}")
            return (self.internal_generator.internal_number())
