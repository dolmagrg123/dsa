"""
Author: DG
Version: 2.0
Date: August 2025
Purpose: Entry point and orchestrator for the number guessing game.
         Coordinates all game components including level selection,
         number generation, gameplay, and leaderboard management.
"""

from random_number_generator import RandomNumberGenerator
from level_manager import LevelManager
from score_manager import ScoreManager
from game import Game

class Main:
    """
    Main application controller and entry point.
    
    Coordinates all game components and manages the overall
    application flow from start to finish.
    """

    def __init__(self) -> None:
        """
        Initialize the main application controller.
        
        Sets up all necessary classes and initializes
        instance variables.
        
        Returns:
            None
        """
        self.level_manager = LevelManager()
        self.generator = None
        self.target_combination  = None
        self.score_manager = ScoreManager()

    def start_game(self) -> None:
        """
        Start and orchestrate the complete game session.
        
        Handles level selection, random number generation,
        gameplay execution, and leaderboard management.
        
        Returns:
            None
        """
        #set values of num, min, max based on the level user chooses
        length, min_val, max_val = self.level_manager.get_settings()

        #generate the random numbers
        self.generator = RandomNumberGenerator(length,min_val,max_val)
        self.target_combination  = self.generator.generate_random_integers()

        #start game
        game = Game(length, min_val, max_val, self.target_combination)
        final_score = game.game_plan()    

        # Leaderboard update
        username = input("\nEnter your username for the leaderboard: ")
        player_rank, total_players = self.score_manager.add_score(username, final_score)
        self.score_manager.display_leaderboard()

        print(f"\nYou are ranked #{player_rank} out of {total_players} players.")
           

if __name__ == "__main__":
    start = Main()
    start.start_game()