class InputValidation:

    def __init__(self, num, min, max):
        self.num = num
        self.min = min
        self.max = max

    def input_validator(self):
        while True:
            user_guess_digits = input(f"Guess the combination (Hint: total {self.num} digits, each digit between {self.min} to {self.max}):")
            if len(user_guess_digits) != self.num:
                print(f"Invalid input: Please enter exactly {self.num} digits.")
                continue
            if not user_guess_digits.isdigit():
                print("Invalid input: Please enter only digits.")
                continue
            user_input_list = [int(digit) for digit in user_guess_digits]
            if any(digit < self.min or digit > self.max for digit in user_input_list):
                print(f"Invalid input: Each digit must be between {self.min} and {self.max}.")
                continue
            return user_input_list
    
