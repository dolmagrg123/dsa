class UserInput:


    def input_validator(self):
        while True:
            user_guess_digits = input("Guess the combination (Hint: total 4 digits, each digit between 0 to 7):")
            if len(user_guess_digits) != 4:
                print("Invalid input: Please enter exactly 4 digits.")
                continue
            if not user_guess_digits.isdigit():
                print("Invalid input: Please enter only digits.")
                continue
            user_input_list = [int(digit) for digit in user_guess_digits]
            if any(digit < 0 or digit > 7 for digit in user_input_list):
                print("Invalid input: Each digit must be between 0 and 7.")
                continue
            return user_input_list
    
