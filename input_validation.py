"""
Author: DG
Version: 2.0
Date: August 2025
Purpose: Handles user input validation for the number guessing game.
         Ensures user guesses meet length, digit, and range requirements
         before passing to game logic.
"""

class InputValidation:

    def __init__(self, length, min_val, max_val):
        self.length = length
        self.min_val = min_val
        self.max_val = max_val

    def input_validator(self):
        while True:
            user_guess_digits = input(f"Guess the combination (Hint: total {self.length} digits, each digit from {self.min_val} to {self.max_val}):")
            if len(user_guess_digits) != self.length:
                print(f"Invalid input: Please enter exactly {self.length} digits.")
                continue
            if not user_guess_digits.isdigit():
                print("Invalid input: Please enter only digits.")
                continue
            user_input_list = [int(digit) for digit in user_guess_digits]
            if any(digit < self.min_val or digit > self.max_val for digit in user_input_list):
                print(f"Invalid input: Each digit must be between {self.min_val} and {self.max_val}.")
                continue
            return user_input_list
    
