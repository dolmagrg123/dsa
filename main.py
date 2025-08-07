"""
Author: DG
Version: 3.0
Date: August 2025
Purpose: Entry point and orchestrator for the number guessing game.
         Coordinates all game components including level selection,
         number generation, gameplay, multiplayer-selection, and leaderboard management.
"""
from level_manager import LevelManager
from random_number_generator import RandomNumberGenerator
from score_manager import ScoreManager
from game import Game
import getpass

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

        print("Welcome to the Number Guessing Game!")
        print("Choose game mode:")
        print("1. Single Player")
        print("2. Multiplayer (One player sets the code, the other guesses)")

        while True:
            mode_choice = input("Enter choice (1 or 2): ")
            if mode_choice in ['1', '2']:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
                
        #set values of num, min, max based on the level user chooses
        length, min_val, max_val = self.level_manager.get_settings()

        if mode_choice == '1':
            #generate the random numbers
            self.generator = RandomNumberGenerator(length,min_val,max_val)
            self.target_combination  = self.generator.generate_random_integers()
            print("\n Starting Single Player Game!!! ")
        else:
            # Get target combination from first player for local multiplayer
            while True:
                combination_str = getpass.getpass(f"\nPlayer 1: Enter the target combination of {length} numbers (between {min_val} and {max_val}, space-separated): ")
                try:
                    self.target_combination = [int(x) for x in combination_str.split()]
                    if len(self.target_combination) == length and all(min_val <= num <= max_val for num in self.target_combination):
                        break
                    else:
                        print(f"Invalid input. Please enter {length} numbers between {min_val} and {max_val}, space-separated.")
                except ValueError:
                    print("Invalid input. Please enter numbers separated by spaces.")
            print("\nStarting Multiplayer game. Player 2, it's your turn to guess!")

        #start game
        game = Game(length, min_val, max_val, self.target_combination)
        final_score = game.game_plan()    

        # Leaderboard update
        username = input("\nEnter your username for the leaderboard: ")
        player_rank, total_players = self.score_manager.add_score(username, final_score)
        self.score_manager.display_leaderboard()

        print(f"\n{username}, You are ranked #{player_rank} out of {total_players} players.")
           

if __name__ == "__main__":
    start = Main()
    start.start_game()
    while True:
        start.start_game()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break