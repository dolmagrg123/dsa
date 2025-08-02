class UserInput:


    def input_validator(self):
        while True:
            guess = input("Guess the combination (Hint: total 4 digits, each digit between 0 to 7):")
            if len(guess) != 4:
                print("Invalid input: Please enter exactly 4 digits.")
                continue
            if not guess.isdigit():
                print("Invalid input: Please enter only digits.")
                continue
            user_input_list = [int(digit) for digit in guess]
            if any(digit < 0 or digit > 7 for digit in user_input_list):
                print("Invalid input: Each digit must be between 0 and 7.")
                continue
            return user_input_list
    
