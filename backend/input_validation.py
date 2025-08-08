"""
Author: DG
Version: 2.0
Date: August 2025
Purpose: Handles user input validation for the number guessing game.
         Ensures user guesses meet length, digit, and range requirements
         before passing to game logic.
"""
from typing import List

class InputValidation:

    """
    Validates user input for the number guessing game.
    
    Ensures that user guesses meet the specified criteria including
    length, digit format, and value range requirements.
    """

    def __init__(self, length: int, min_val: int, max_val: int) -> None:
        """
        Initialize the input validator with game parameters.
        
        Args:
            length (int): Required length of the guess
            min_val (int): Minimum allowed digit value
            max_val (int): Maximum allowed digit value
            
        Returns:
            None
        """
        self.length = length
        self.min_val = min_val
        self.max_val = max_val

    def input_validator(self) -> List[int]:
        """
        Validate and collect user input for the game.
        
        Continuously prompts the user for input until a valid guess is provided.
        Validates length, digit format, and value range.
        
        Returns:
            List[int]: List of validated integers representing the user's guess
            
        Raises:
            ValueError: If digit conversion fails (handled internally)
        """
        while True:
            user_guess_digits = input(f"Guess the combination (Hint: total {self.length} digits, each digit from {self.min_val} to {self.max_val}):")
            
            #Check length requirement
            if len(user_guess_digits) != self.length:
                print(f"Invalid input: Please enter exactly {self.length} digits.")
                continue

            #Check to ensure all inputs are only digits
            if not user_guess_digits.isdigit():
                print("Invalid input: Please enter only digits.")
                continue

            #Convert to list of integers
            user_input_list = [int(digit) for digit in user_guess_digits]

            #Check value range for each user input
            if any(digit < self.min_val or digit > self.max_val for digit in user_input_list):
                print(f"Invalid input: Each digit must be between {self.min_val} and {self.max_val}.")
                continue
            return user_input_list
    
