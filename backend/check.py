"""
Author: DG
Version: 2.0
Date: August 2025
Purpose: Provides feedback mechanism for the number guessing game.
         Compares user guesses against target combination and returns
         counts of correct numbers and correct location.
"""

from collections import Counter
from typing import List, Tuple

class Checker:
    """
    Analyzes user guesses against target combinations and provides feedback.
    
    This class compares a user's guess with the target combination and provides
    detailed feedback about correct numbers and their location.
    """

    def __init__(self, user_guess_digits:List[int], target_digits:List[int]) -> None:
        """
        Initialize the Checker with user guess and target digits.
        
        Args:
            user_guess_digits (List[int]): List of integers representing user's guess
            target_digits (List[int]): List of integers representing the target combination
        
        Returns:
            None
        """
        self.user_guess_digits = user_guess_digits
        self.target_digits = target_digits

    def feedback_provider(self) -> Tuple[int, int, str]:

        """
        Provide detailed feedback on total correct numbers and total correct location
        
        Compares the user's guess with the target combination and returns:
        - Total count of correct digits (regardless of location)
        - Count of digits in correct location
        - Descriptive feedback message
        
        Returns:
            Tuple[int, int, str]: A tuple containing:
                - total_correct_digits: Number of correct digits found
                - correct_location_count: Number of digits in correct location
                - feedback_message: Descriptive feedback string
                
        Raises:
            ValueError: If input processing fails
        """
            
        try:
            correct_location_count = 0
            total_correct_digits = 0

            #create frequency counters for user input and random generated number
            user_counts = Counter(self.user_guess_digits )
            target_counts  = Counter(self.target_digits)

            # Check for numbers in correct location and keep count
            for i in range(len(self.user_guess_digits)):
                if self.user_guess_digits[i] == self.target_digits[i]:
                    correct_location_count += 1
                    total_correct_digits += 1
                    user_counts[self.user_guess_digits[i]] -= 1
                    target_counts[self.target_digits[i]] -= 1

            # Check for correct numbers in wrong location
            for digit in self.user_guess_digits:
                if user_counts[digit] > 0 and target_counts[digit] > 0:
                    total_correct_digits += 1
                    user_counts[digit] -= 1
                    target_counts[digit] -= 1
            
            #Return feedback message and counts of correct numbers
            if total_correct_digits == 0 and correct_location_count == 0:
                return 0, 0, "All digits are incorrect"
            else:
                return total_correct_digits, correct_location_count, f"{total_correct_digits} correct number and {correct_location_count} correct location"
        except ValueError as e:
            return 0, 0, f"Error processing input: {e}"

    def correct_combination(self) -> bool:
        """
        Check if the user's guess matches the target combination exactly.
        
        Returns:
            bool: True if all digits match in correct positions, False otherwise
        """
        if self.target_digits == self.user_guess_digits:
            return True
        else:
            return False
