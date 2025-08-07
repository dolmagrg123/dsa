"""
Author: DG
Version: 2.0
Date: August 2025
Purpose: Manages player scores and leaderboard functionality.
         Handles score persistence to JSON file, ranking system,
         and leaderboard display for the number guessing game.
"""

import json
import os
from typing import List, Dict, Tuple, Union

SCORE_FILE = "scores.json"

class ScoreManager:
    """
    Manages player scores and leaderboard functionality.
    
    Handles loading, saving, and displaying player scores with
    persistent storage using JSON format.
    """

    def __init__(self, file_path: str = SCORE_FILE) -> None:
        """
        Initialize the score manager.
        
        Args:
            file_path (str): Path to the JSON file for score storage
            
        Returns:
            None
        """
        self.file_path = file_path
        self.scores = self.load_scores()

    #read the existing score json file
    def load_scores(self) -> List[Dict[str, Union[str, int]]]:
        """
        Load existing scores from the JSON file.
        
        Attempts to read and parse the scores file. Returns an empty
        list if the file doesn't exist or contains invalid JSON.
        
        Returns:
            List[Dict[str, Union[str, int]]]: List of score entries, each containing
                username and score information
            Each item in that list is a dictionary where:
            Keys are strings (str)
            Values can be either:
                - a string (str)
                - or an integer (int)
                
        Raises:
            json.JSONDecodeError: If file contains invalid JSON (handled internally)
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return [] # return empty list if file does not exists/is empty
        return []

    #save score into the json file
    def save_scores(self) -> None:
        """
        Save current scores to the JSON file.
        
        Writes the current scores list to the file in JSON format
        with proper indentation for readability.
        
        Returns:
            None
        """
        with open(self.file_path, "w") as f:
            json.dump(self.scores, f, indent=4)

    def add_score(self, username: str, score: int) -> Tuple[int, int]:
        """
        Add a new score entry and return player ranking.
        
        Inserts the new score in the correct position to maintain
        descending order and saves the updated scores.
        
        Args:
            username (str): Player's username
            score (int): Player's achieved score
            
        Returns:
            Tuple[int, int]: A tuple containing:
                - player_rank: Player's rank
                - total_players: Total number of players
        """
        new_entry = {
            "username": username,
            "score": score,
        }

        # insert score into correct position
        for i in range(len(self.scores)):
            if score > self.scores[i]["score"]: 
                self.scores.insert(i, new_entry)
                break
        else:
            self.scores.append(new_entry) # adds to the end

        self.save_scores()

        # Get player's rank
        player_rank = self.scores.index(new_entry) + 1
        return player_rank, len(self.scores)

    def display_leaderboard(self) -> None:
        """
        Display the top 10 players on the leaderboard.
        
        Prints a formatted leaderboard showing the top 10 scores
        with rankings, usernames, and points.
        
        Returns:
            None
        """
        print("\n ---------------  Top 10 Leaderboard -----------------")
        top_scores = self.scores[:10]
        for i in range(len(top_scores)):
            entry = top_scores[i]
            print(f"{i + 1}. {entry['username']} - {entry['score']} points")

