import random

class InternalGenerator:

    def __init__(self, num, min_val, max_val):
        self.num = num
        self.min_val = min_val
        self.max_val = max_val
        
    def internal_number(self):
        print("Generating random number internally!!!")
        number = [random.randint(self.min_val, self.max_val) for _ in range(self.num)]
        return number
