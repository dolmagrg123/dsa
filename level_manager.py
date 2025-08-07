"""
Author: DG
Version: 2.0
Date: August 2025
Purpose: Manages difficulty levels and game configuration settings.
         User can choose between easy, medium, and difficult modes which decides
         combination length and digit ranges.
"""

from typing import Tuple

class LevelManager:
    """
    Manages game difficulty levels and their corresponding settings.
    
    Provides different difficulty levels with varying combination lengths
    and digit ranges to create different gameplay experiences.
    """
    def __init__(self) -> None:
        """
        Initialize the level manager with default settings.
        
        Sets up default values and predefined level configurations.
        
        Returns:
            None
        """
        self.length = 4 
        self.min_val = 0
        self.max_val = 7
        self.level_settings = {
            "easy": (4, 0, 7),
            "medium": (8, 0, 7)
        }

    def choose_level(self) -> None:
        """
        Handle user level selection and update game settings accordingly.
        
        Prompts the user to choose a difficulty level and updates the
        instance variables with the corresponding settings.
        
        Returns:
            None
        """
        while True:
            level = input("Choose a level (easy, medium, difficult): ").lower()

            if level in self.level_settings:
                self.length, self.min_val, self.max_val = self.level_settings[level]
                break
            elif level == "difficult":
                self.min_val = 0
                self.max_val = 9
                self.get_difficult_level_settings()
                break
            else:
                print("Invalid level.")

    def get_difficult_level_settings(self) -> None:
        """
        Handle custom settings for difficult level.
        
        Prompts the user to specify a custom combination length
        for the difficult difficulty level.
        
        Returns:
            None
            
        Raises:
            ValueError: If user input is not a valid integer (handled internally)
        """
        while True:
            try:
                length = int(input("Enter desired combination length (greater than 8): "))
                if length > 8:
                    self.length = length
                    break
                else:
                    print("Length must be greater than 8.")
            except ValueError:
                print("Invalid input. Please enter a number for length.")

    def get_settings(self) -> Tuple[int, int, int]:
        """
        Get the configured game settings after level selection.
        
        Calls the level selection process and returns the final
        configuration values.
        
        Returns:
            Tuple[int, int, int]: A tuple containing:
                - length: Number of digits in the combination
                - min_val: Minimum allowed digit value
                - max_val: Maximum allowed digit value
        """
        self.choose_level()
        return self.length, self.min_val, self.max_val
