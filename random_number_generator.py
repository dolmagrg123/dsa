from internal_generator import InternalGenerator
import requests
import datetime
# import json
#Import os to secure our APIKEY as env variable
# import os 

class RandomNumberGenerator:
    def __init__(self, num, min_val, max_val):
        self.url = "https://www.random.org/integers/"
        self.num = num
        self.min_val = min_val
        self.max_val = max_val
        self.internal_num = InternalGenerator(self.num, self.min_val, self.max_val)

    def generate_random_integers(self):
        params = {
            "num": self.num,        # Number of integers requested
            "min_val": self.min_val,        # The smallest value returned
            "max_val": self.max_val,        # The largest value returned
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

                random_data = []
                for num in numbers:
                    num = num.strip()
                    if num.isdigit():
                        random_data.append(int(num))
                    else:
                        with open("error.log", "a") as f: #append error into error.log
                            f.write(f"\n Invalid value in server response: {num}")
                if random_data:
                    print(random_data)
                    return random_data
                else:
                        with open("error.log", "a") as f:
                            f.write(f"\n No valid numbers found in server response.")
                        return None
                
            else:
                with open("error.log", "a") as f:
                    f.write(f"\n API_URL ERROR: Date and Time: {datetime.datetime.now()} \n Error Code: {response.status_code}")

                #return list of random generated number without using API
                return (self.internal_num.internal_number())
                
        except requests.exceptions.RequestException as e:
            print(f"Error calling random.org API: {e}")
            return None # Return None to indicate an error
