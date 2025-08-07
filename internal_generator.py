"""
Author: DG
Version: 2.0
Date: August 2025
Purpose: Fallback random number generator for the number guessing game.
         Generates random target combinations locally when external API
         is unavailable or fails.
"""
import random
from typing import List

class InternalGenerator:
    """
    Generates random number combinations internally as a fallback mechanism.
    
    Used when external random number generation services are unavailable
    or fail to provide valid responses.
    """

    def __init__(self, length: int, min_val: int, max_val: int) -> None:
        """
        Initialize the internal random number generator.
        
        Args:
            length (int): Number of digits to generate
            min_val (int): Minimum value for each digit
            max_val (int): Maximum value for each digit
            
        Returns:
            None
        """
        self.length = length
        self.min_val = min_val
        self.max_val = max_val
        
    def internal_number(self) -> List[int]:
        """
        Generate a random number combination internally.
        
        Creates a list of random integers within the specified range
        and length requirements.
        
        Returns:
            List[int]: List of randomly generated integers
        """
        
        print("Generating random number internally!!!")
        number = [random.randint(self.min_val, self.max_val) for _ in range(self.length)]
        return number
