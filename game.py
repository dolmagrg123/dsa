"""
Author: DG
Version: 2.0
Date: August 2025
Purpose: Main game logic controller for the number guessing game.
         Manages game flow, takes user input, calculates score, and 
         coordinates feedback components.
"""
from check import Checker
from input_validation import InputValidation
from typing import List
import time
class Game:
    """
    Main game controller that orchestrates the gameplay loop.
    
    Manages the core game logic including user input, feedback,
    scoring, and win/lose conditions.
    """

    def __init__(self, length: int, min_val: int, max_val: int, target_combination: List[int]) -> None:
        """
        Initialize the game with specified parameters.
        
        Args:
            length (int): Length of the target combination
            min_val (int): Minimum allowed digit value
            max_val (int): Maximum allowed digit value
            target_combination (List[int]): The target combination to guess
            
        Returns:
            None
        """
        self.guesses_left = 10
        self.length = length
        self.min_val = min_val
        self.max_val = max_val
        self.target_combination = target_combination
        self.player_score = 0
        self.hinted_positions = set() # To keep track of hinted positions
        self.input_validator  = InputValidation(length, min_val, max_val)
        
    def game_plan(self)-> int:
        """
        Main game loop that handles calling all necessary classes to run the game"
        Allows players to take hints.

        Returns:
            int: Final player score
        """
        start_time = time.time()
        time_limit = 300 #seconds

        while self.guesses_left > 0:
            elapsed_time = time.time() - start_time
            if elapsed_time > time_limit:
                print("\nTime's up! You ran out of time.")
                self.guesses_left = 0 # End the game loop
                break

            while True:
                time_remaining = max(0, time_limit - int(elapsed_time))
                hint_choice = input(f"Time remaining: {time_remaining} seconds. Do you want a hint? (y/n): ").lower()
                if hint_choice in ['y', 'n']:
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

            if hint_choice == 'y':
                hint_provided = False
                for i in range(self.length):
                    # Check if the position hasn't been hinted
                    if i not in self.hinted_positions: 
                        print(f"Hint: The number at position {i+1} is {self.target_combination[i]}.")
                        self.player_score = max(0, self.player_score - 10) # Deduct points, ensure score doesn't go below 0
                        self.hinted_positions.add(i)
                        hint_provided = True
                        break # Provide only one hint per request
                if not hint_provided:
                    print("No new hints available at this time.")
                continue # Skip the guessing process for this turn if a hint was requested
            self.guesses_left -= 1
            user_guess = self.input_validator .input_validator()

            #pass the two list of random generated numbers and combination guessed by user
            checker = Checker(user_guess,self.target_combination)
            correct_number, correct_location, feedback = checker.feedback_provider()
            
            self.player_score += correct_number + correct_location
            print(feedback)
            print(f"Your Current score: {self.player_score}")

            if checker.correct_combination():
                print("\n---------------YAYYYYY-----------------")
                print("Congratulations!!! You have guessed the correct combination")
                break  
            if self.guesses_left > 0:
                print(f"You have {self.guesses_left} guesses remaining")
            else:
                print(f"The correct combination is {self.target_combination}")
                print("Sorry!!! You ran out of guesses. Please TRY AGAIN")

        # End-game bonus
        self.player_score += self.guesses_left * 10 * self.length
        print(f"\nFinal score: {self.player_score}")

        return self.player_score


