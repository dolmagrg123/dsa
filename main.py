from generator import RandomNumberGenerator
from check import GuessChecker

class Game:

    def __init__(self):
        self.generator = RandomNumberGenerator()
        self.checker =GuessChecker()

    def start_game(self):
        random_generated_number = self.generator.generate_random_integers()
        no_of_guess_reamining =10

        for i in range(10):
            no_of_guess_reamining -= 1
            guess = input("Guess the combination (Hint: each digit between 0 to 7):")
            user_input_list= [int(digit) for digit in guess]

            if (self.checker.correct_combination(user_input_list,random_generated_number )) == True:
                break
            else:
                print (f"You have {no_of_guess_reamining} guesses remaining")
        
        print (f"The correct combination is {random_generated_number}")
        

if __name__ == "__main__":
    game = Game()
    game.start_game()