import random

class InternalGenerator:

    def __init__(self, length, min_val, max_val):
        self.length = length
        self.min_val = min_val
        self.max_val = max_val
        
    def internal_number(self):
        print("Generating random number internally!!!")
        number = [random.randint(self.min_val, self.max_val) for _ in range(self.length)]
        return number
