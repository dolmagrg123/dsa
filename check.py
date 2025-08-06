"""
Author: DG
Version: 2.0
Date: August 2025
Purpose: Provides feedback mechanism for the number guessing game.
         Compares user guesses against target combination and returns
         counts of correct numbers and correct positions.
"""

from collections import Counter
from typing import List, Tuple

class Checker:

    def __init__(self, user_guess_digits:List[int], target_digits:List[int]) -> None:
        self.user_guess_digits = user_guess_digits
        self.target_digits = target_digits

    def feedback_provider(self) -> Tuple[int, int, str]:
            """
            Analyze user guess against target and provide detailed feedback.
            
            Returns:
                Tuple[int, int, str]: (total_correct_digits, correct_position_count, feedback_message)
                
            Raises:
                ValueError: If input processing fails
            """
            try:
                correct_position_count = 0
                total_correct_digits = 0

                user_counts = Counter(self.user_guess_digits )
                target_counts  = Counter(self.target_digits)

                # Check for correct location and number
                for i in range(len(self.user_guess_digits)):
                    if self.user_guess_digits[i] == self.target_digits[i]:
                        correct_position_count += 1
                        total_correct_digits += 1
                        user_counts[self.user_guess_digits[i]] -= 1
                        target_counts[self.target_digits[i]] -= 1

                # Check for correct numbers (wrong location)
                for digit in self.user_guess_digits:
                    if user_counts[digit] > 0 and target_counts[digit] > 0:
                        total_correct_digits += 1
                        user_counts[digit] -= 1
                        target_counts[digit] -= 1
                  
                if total_correct_digits == 0 and correct_position_count == 0:
                    return 0, 0, "all incorrect"
                else:
                    return total_correct_digits, correct_position_count, f"{total_correct_digits} correct number and {correct_position_count} correct location"
            except ValueError as e:
                return 0, 0, f"Error processing input: {e}"



    def correct_combination(self) -> bool:
        if self.target_digits == self.user_guess_digits:
            return True
        else:
            return False
