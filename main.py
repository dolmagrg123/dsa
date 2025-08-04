from generator import RandomNumberGenerator
from check import GuessChecker
from input_validation import UserInput
from level_manager import LevelManager

class Game:

    def __init__(self):
        self.level_manager = LevelManager()
        num, min, max = self.level_manager.get_settings()
        self.generator = RandomNumberGenerator(num,min,max)
        self.user_input = UserInput(num,min,max)
        self.remaining_guesses = 10
        self.target_combination  = None

    def start_game(self):

        self.target_combination  = self.generator.generate_random_integers()
    
        for i in range(10):
            self.remaining_guesses -= 1

            user_guess = self.user_input.input_validator()
            checker =GuessChecker(user_guess,self.target_combination)

            if (checker.correct_combination()) == True:
                break
            else:
                print (f"You have {self.remaining_guesses} guesses remaining")
        
        print (f"The correct combination is {self.target_combination }")
        

if __name__ == "__main__":
    game = Game()
    game.start_game()