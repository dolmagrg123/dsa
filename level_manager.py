class LevelManager:
    def __init__(self):
        self.num = 4 
        self.min_val = 0
        self.max_val = 7
        self.level_settings = {
            "easy": (4, 0, 7),
            "medium": (8, 0, 7)
        }

    #Based on user input, this function will set num, min and max
    def choose_level(self):
        while True:
            level = input("Choose a level (easy, medium, difficult): ").lower()
            if level in self.level_settings:
                self.num, self.min_val, self.max_val = self.level_settings[level]
                break
            elif level == "difficult":
                self.min_val = 0
                self.max_val = 9
                self.get_difficult_level_settings()
                break
            else:
                print("Invalid level.")

    def get_difficult_level_settings(self):
        while True:
            try:
                length = int(input("Enter desired combination length (greater than 8): "))
                if length > 8:
                    self.num = length
                    break
                else:
                    print("Length must be greater than 8.")
            except ValueError:
                print("Invalid input. Please enter a number for length.")

    #calls choose_level function to get values of num, min and max and returns the values
    def get_settings(self):
        self.choose_level()
        return self.num, self.min_val, self.max_val
