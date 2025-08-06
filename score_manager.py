import json
import os

SCORE_FILE = "scores.json"

class ScoreManager:
    def __init__(self, file_path=SCORE_FILE):
        self.file_path = file_path
        self.scores = self.load_scores()

    #read the existing score json file
    def load_scores(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return [] # return empty list if file does not exists/is empty
        return []

    #save score into the json file
    def save_scores(self):
        with open(self.file_path, "w") as f:
            json.dump(self.scores, f, indent=4)

    def add_score(self, username, score):
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

    def display_leaderboard(self):
        print("\n ---------------  Top 10 Leaderboard -----------------")
        top_scores = self.scores[:10]
        for i in range(len(top_scores)):
            entry = top_scores[i]
            print(f"{i + 1}. {entry['username']} - {entry['score']} points")

