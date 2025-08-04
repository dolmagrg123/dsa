import random

class InternalRandom:

    def __init__(self, num, min, max):
        self.num = num
        self.min = min
        self.max = max
        
    def internal_number(self):
        print("Generating random number internally!!!")
        number = [random.randint(self.min, self.max) for _ in range(self.num)]
        # print(f"Internally generated random number is{number}")
        return number
