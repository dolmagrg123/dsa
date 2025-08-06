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

class Game:
    def __init__(self, length, min_val, max_val, target_combination):
        self.guesses_left = 10
        self.length = length
        self.min_val = min_val
        self.max_val = max_val
        self.target_combination = target_combination
        self.player_score = 0
        self.input_validator  = InputValidation(length, min_val, max_val)
        
    def game_plan(self):
        while self.guesses_left > 0:
            self.guesses_left -= 1
            user_guess = self.input_validator .input_validator()

            #pass the two list of random generated numbers and combination guessed by user
            checker = Checker(user_guess,self.target_combination)
            correct_number, correct_location, feedback = checker.feedback_provider()
            self.player_score += correct_number + correct_location
            print(feedback)
            print(f"Your Current score: {self.player_score}")

            if checker.correct_combination():
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


