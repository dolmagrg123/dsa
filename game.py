from check import Checker
from input_validation import InputValidation

class Game:
    def __init__(self, length, min_val, max_val, target_combination):
        self.remaining_guesses = 10
        self.length = length
        self.min_val = min_val
        self.max_val = max_val
        self.target_combination = target_combination
        self.score = 0
        self.user_input = InputValidation(length, min_val, max_val)
        
    def game_plan(self):
        while self.remaining_guesses > 0:
            self.remaining_guesses -= 1
            user_guess = self.user_input.input_validator()

            #pass the two list of random generated numbers and combination guessed by user
            checker = Checker(user_guess,self.target_combination)
            correct_number, correct_location, feedback = checker.feedback_provider()
            self.score += correct_number + correct_location
            print(feedback)
            print(f"Current score: {self.score}")

            if checker.correct_combination():
                print("Congratulations!!! You have guessed the correct combination")
                break  

            if self.remaining_guesses > 0:
                print(f"You have {self.remaining_guesses} guesses remaining")
            else:
                print(f"The correct combination is {self.target_combination}")
                print("Sorry!!! You ran out of guesses. Please TRY AGAIN")

        # End-game bonus
        self.score += self.remaining_guesses * 10 * self.length
        print(f"\nFinal score: {self.score}")

        return self.score


