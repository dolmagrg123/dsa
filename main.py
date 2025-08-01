from generator import generate_random_integers
from check import correct_combination

def start_game():
    random_generated_number = generate_random_integers()
    no_of_guess_reamining =10

    for i in range(10):
        no_of_guess_reamining -= 1
        guess = input("Guess the combination (Hint: each digit between 0 to 7):")
        user_input_list= [int(digit) for digit in guess]

        if (correct_combination(user_input_list,random_generated_number )) == True:
            break
        else:
            print (f"You have {no_of_guess_reamining} guesses remaining")
    
    print (f"The correct combination is {random_generated_number}")
    

start_game()