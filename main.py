from random_number_generator import RandomNumberGenerator
from check import Checker
from input_validation import InputValidation
from level_manager import LevelManager

class Game:

    def __init__(self):
        self.level_manager = LevelManager()
        self.generator = None
        self.user_input = None
        self.remaining_guesses = 10
        self.target_combination  = None


    def start_game(self):
        #set values of num, min, max based on the level user chooses
        num, min, max = self.level_manager.get_settings()

        self.generator = RandomNumberGenerator(num,min,max)
        self.target_combination  = self.generator.generate_random_integers() # random number generated
        self.user_input = InputValidation(num,min,max) # combination guessed by user
    
        while self.remaining_guesses > 0:
            self.remaining_guesses -= 1
            user_guess = self.user_input.input_validator()

            #pass the two list of random generated numbers and combination guessed by user
            checker = Checker(user_guess,self.target_combination)

            is_correct, message = checker.correct_combination()
            print(message)  # Show feedback from GuessChecker

            if is_correct:
                break
            elif self.remaining_guesses > 0:
                print(f"You have {self.remaining_guesses} guesses remaining")
            else:
                print(f"The correct combination is {self.target_combination}")
                print("Sorry!!! You ran out of guesses. Please TRY AGAIN")
        
        
        

if __name__ == "__main__":
    game = Game()
    game.start_game()