from random_number_generator import RandomNumberGenerator
from level_manager import LevelManager
from score_manager import ScoreManager
from game import Game

class Main:
    def __init__(self):
        self.level_manager = LevelManager()
        self.generator = None
        self.target_combination  = None
        self.score_manager = ScoreManager()

    def start_game(self):
        #set values of num, min, max based on the level user chooses
        num, min_val, max_val = self.level_manager.get_settings()

        #generate the random numbers
        self.generator = RandomNumberGenerator(num,min_val,max_val)
        self.target_combination  = self.generator.generate_random_integers()

        #start game
        game = Game(num, min_val, max_val, self.target_combination)
        final_score = game.game_plan()    

        # Leaderboard update
        username = input("\nEnter your username for the leaderboard: ")
        player_rank, total_players = self.score_manager.add_score(username, final_score)
        self.score_manager.display_leaderboard(highlight_user=username)

        if player_rank > 10:
            print(f"\nYou are ranked #{player_rank} out of {total_players} players.")
           

if __name__ == "__main__":
    start = Main()
    start.start_game()