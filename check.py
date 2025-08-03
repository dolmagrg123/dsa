class GuessChecker:

    def __init__(self, user_guess_digits, target_digits):
        self.user_guess_digits = user_guess_digits
        self.target_digits = target_digits

    def feedback_provider(self):
            correct_location = 0
            correct_number = 0

            #create copies of the list to avoid modifying the original list
            user_copy = list(self.user_guess_digits )
            random_copy  = list(self.target_digits)

            #checking to see if the numbers are in correct location
            index = 0
            for i in user_copy:
                if i == random_copy[index]:
                    correct_location += 1
                    correct_number +=1
                    random_copy[index]="matched" # marked to make sure it is not counted again
                    user_copy[index] ="ignore"
                index +=1 #increment index for the list to make sure correct data is compared

            for i in range(len(user_copy)):
                for j in range (len(random_copy)):
                    if user_copy[i] == random_copy[j]:
                        correct_number += 1
                        random_copy[j]="matched"
                        user_copy[i] ="ignore"
            
            #print all incorrect if none of the numbers and location matches
            if correct_number == 0 and correct_location == 0:
                print ("all incorrect")
            else:
                print(f" {correct_number} correct number and {correct_location} correct location")


    def correct_combination(self):
        if self.target_digits == self.user_guess_digits:
            print("Congratulations!!! You have guessed the correct combination")
            return True
            
        else:
            self.feedback_provider()
            return False
