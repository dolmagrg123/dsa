from collections import Counter

class Checker:

    def __init__(self, user_guess_digits, target_digits):
        self.user_guess_digits = user_guess_digits
        self.target_digits = target_digits

    def feedback_provider(self):
            try:
                correct_location = 0
                correct_number = 0

                user_counts = Counter(self.user_guess_digits )
                target_counts  = Counter(self.target_digits)

                # Check for correct location and number
                for i in range(len(self.user_guess_digits)):
                    if self.user_guess_digits[i] == self.target_digits[i]:
                        correct_location += 1
                        correct_number += 1
                        user_counts[self.user_guess_digits[i]] -= 1
                        target_counts[self.target_digits[i]] -= 1

                # Check for correct numbers (wrong location)
                for digit in self.user_guess_digits:
                    if user_counts[digit] > 0 and target_counts[digit] > 0:
                        correct_number += 1
                        user_counts[digit] -= 1
                        target_counts[digit] -= 1
                  
                if correct_number == 0 and correct_location == 0:
                    return 0, 0, "all incorrect"
                else:
                    return correct_number, correct_location, f"{correct_number} correct number and {correct_location} correct location"
            except ValueError as e:
                return 0, 0, f"Error processing input: {e}"



    def correct_combination(self):
        if self.target_digits == self.user_guess_digits:
            return True
        else:
            return False
