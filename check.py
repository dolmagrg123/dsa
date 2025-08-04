from collections import Counter

class GuessChecker:

    def __init__(self, user_guess_digits, target_digits):
        self.user_guess_digits = user_guess_digits
        self.target_digits = target_digits

    def feedback_provider(self):
            try:
                correct_location = 0
                correct_number = 0

                #create copies of the list to avoid modifying the original list
                user_counts = Counter(self.user_guess_digits )
                target_counts  = Counter(self.target_digits)
                # print(user_counts)
                # print(random_counts)

                # Check for correct location and update frequency maps
                for i in range(len(self.user_guess_digits)):
                    if self.user_guess_digits[i] == self.target_digits[i]:
                        correct_location += 1
                        correct_number += 1
                        # Decrement counts for matched digits
                        user_counts[self.user_guess_digits[i]] -= 1
                        target_counts[self.target_digits[i]] -= 1

                # Check for correct numbers (wrong location) using updated frequency maps
                for digit in self.user_guess_digits:
                    if user_counts[digit] > 0 and target_counts[digit] > 0:
                        correct_number += 1
                        # Decrement counts as these digits are now accounted for
                        user_counts[digit] -= 1
                        target_counts[digit] -= 1
    

                # #checking to see if the numbers are in correct location
                # index = 0
                # for i in user_copy:
                #     if i == random_copy[index]:
                #         correct_location += 1
                #         correct_number +=1
                #         random_copy[index]="matched" # marked to make sure it is not counted again
                #         user_copy[index] ="ignore"
                #     index +=1 #increment index for the list to make sure correct data is compared

                # for i in range(len(user_copy)):
                #     for j in range (len(random_copy)):
                #         if user_copy[i] == random_copy[j]:
                #             correct_number += 1
                #             random_copy[j]="matched"
                #             user_copy[i] ="ignore"
                
                #print all incorrect if none of the numbers and location matches
                if correct_number == 0 and correct_location == 0:
                    print ("all incorrect")
                else:
                    print(f" {correct_number} correct number and {correct_location} correct location")
            except ValueError as e:
                print(f"Error processing input: {e}")



    def correct_combination(self):
        if self.target_digits == self.user_guess_digits:
            print("Congratulations!!! You have guessed the correct combination")
            return True
        else:
            self.feedback_provider()
            return False
