"""
Flask Web Application for Number Guessing Game
==============================================

Version: 3.1 Web
Date: August 2025
Purpose: Web-based interface using Flask to replace command-line interaction
"""

from flask import Flask, render_template, request, jsonify, session
import time
import secrets
from typing import List, Dict, Any

# Import your existing game modules
from random_number_generator import RandomNumberGenerator
from level_manager import LevelManager
from score_manager import ScoreManager
from game import Game
from check import Checker
# from input_validation import InputValidation

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generate a secure secret key

class WebGameManager:
    """
    Manages web-based game sessions and state.
    
    Handles game initialization, state management, and coordination
    between Flask routes and existing game logic.
    """
    
    def __init__(self):
        """Initialize the web game manager."""
        self.score_manager = ScoreManager()
        self.active_games = {}  # Store active game sessions
        
    def create_new_game(self, session_id: str, mode: str, difficulty: str, 
                       custom_length: int = None, target_combination: List[int] = None) -> Dict[str, Any]:
        """
        Create a new game session with specified parameters.
        
        Args:
            session_id: Unique session identifier
            mode: Game mode ('single' or 'multi')
            difficulty: Difficulty level ('easy', 'medium', 'difficult')
            custom_length: Custom length for difficult mode
            target_combination: Pre-set combination for multiplayer
            
        Returns:
            Dict containing game state information
        """
        # Set difficulty parameters
        if difficulty == "easy":
            length, min_val, max_val = 4, 0, 7
        elif difficulty == "medium":
            length, min_val, max_val = 8, 0, 7
        else:  # difficult
            length, min_val, max_val = custom_length or 10, 0, 9
            
        # Generate or set target combination
        if mode == "single" or target_combination is None:
            generator = RandomNumberGenerator(length, min_val, max_val)
            target_combination = generator.generate_random_integers()
        
        # Create game instance
        game = Game(length, min_val, max_val, target_combination)
        
        # Store game state
        game_state = {
            'game': game,
            'target_combination': target_combination,
            'length': length,
            'min_val': min_val,
            'max_val': max_val,
            'mode': mode,
            'difficulty': difficulty,
            'start_time': time.time(),
            'time_limit': 300,  # 5 minutes
            'game_over': False,
            'won': False,
            'guesses': [],
            'feedback_history': []
        }
        
        self.active_games[session_id] = game_state
        return game_state
        
    def get_game_state(self, session_id: str) -> Dict[str, Any]:
        """Get current game state for a session."""
        return self.active_games.get(session_id)
        
    def process_guess(self, session_id: str, guess: str) -> Dict[str, Any]:
        """
        Process a player's guess and return updated game state.
        
        Args:
            session_id: Session identifier
            guess: Player's guess as string
            
        Returns:
            Dict containing updated game state and feedback
        """
        game_state = self.active_games.get(session_id)
        if not game_state or game_state['game_over']:
            return {'error': 'No active game found'}
            
        game = game_state['game']
        
        try:
            # Validate input
            if len(guess) != game_state['length']:
                return {'error': f"Please enter exactly {game_state['length']} digits"}
                
            if not guess.isdigit():
                return {'error': 'Please enter only digits'}
                
            user_guess = [int(digit) for digit in guess]
            
            # Check digit range
            min_val, max_val = game_state['min_val'], game_state['max_val']
            if any(digit < min_val or digit > max_val for digit in user_guess):
                return {'error': f'Each digit must be between {min_val} and {max_val}'}
            
            # Process guess
            game.guesses_left -= 1
            checker = Checker(user_guess, game_state['target_combination'])
            correct_number, correct_location, feedback = checker.feedback_provider()
            
            # Update score
            points_earned = correct_number + correct_location
            game.player_score += points_earned
            
            # Store guess and feedback
            guess_result = {
                'guess': guess,
                'correct_numbers': correct_number,
                'correct_positions': correct_location,
                'feedback': feedback,
                'points_earned': points_earned,
                'total_score': game.player_score
            }
            
            game_state['guesses'].append(guess_result)
            game_state['feedback_history'].append(feedback)
            
            # Check win condition
            if checker.correct_combination():
                game_state['won'] = True
                game_state['game_over'] = True
                # Add bonus points
                bonus = game.guesses_left * 10 * game_state['length']
                game.player_score += bonus
                guess_result['bonus'] = bonus
                guess_result['total_score'] = game.player_score
                
            # Check if out of guesses or time
            elif game.guesses_left <= 0:
                game_state['game_over'] = True
                
            # Update time
            elapsed_time = time.time() - game_state['start_time']
            if elapsed_time >= game_state['time_limit']:
                game_state['game_over'] = True
                
            return {
                'success': True,
                'guess_result': guess_result,
                'game_state': {
                    'guesses_left': game.guesses_left,
                    'score': game.player_score,
                    'game_over': game_state['game_over'],
                    'won': game_state['won'],
                    'time_remaining': max(0, game_state['time_limit'] - elapsed_time)
                }
            }
            
        except Exception as e:
            return {'error': f'Error processing guess: {str(e)}'}
    
    def get_hint(self, session_id: str) -> Dict[str, Any]:
        """
        Provide a hint to the player.
        
        Args:
            session_id: Session identifier
            
        Returns:
            Dict containing hint information and updated score
        """
        game_state = self.active_games.get(session_id)
        if not game_state or game_state['game_over']:
            return {'error': 'No active game found'}
            
        game = game_state['game']
        
        # Find next available hint position
        for i in range(game_state['length']):
            if i not in game.hinted_positions:
                hint_text = f"Position {i+1} is {game_state['target_combination'][i]}"
                game.player_score = max(0, game.player_score - 10)
                game.hinted_positions.add(i)
                
                return {
                    'success': True,
                    'hint': hint_text,
                    'score': game.player_score,
                    'penalty': 10
                }
        
        return {'error': 'No more hints available'}

# Initialize the game manager
game_manager = WebGameManager()

@app.route('/')
def index():
    """Main game page."""
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    """Start a new game session."""
    data = request.get_json()
    
    mode = data.get('mode', 'single')
    difficulty = data.get('difficulty', 'easy')
    custom_length = data.get('custom_length')
    target_combination = data.get('target_combination')
    
    # Generate session ID
    session_id = secrets.token_urlsafe(16)
    session['game_id'] = session_id
    
    try:
        # Create new game
        game_state = game_manager.create_new_game(
            session_id, mode, difficulty, custom_length, target_combination
        )
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'game_info': {
                'length': game_state['length'],
                'min_val': game_state['min_val'],
                'max_val': game_state['max_val'],
                'mode': game_state['mode'],
                'difficulty': game_state['difficulty'],
                'guesses_left': game_state['game'].guesses_left,
                'score': game_state['game'].player_score,
                'time_limit': game_state['time_limit']
            }
        })
        
    except Exception as e:
        return jsonify({'error': f'Failed to start game: {str(e)}'}), 400

@app.route('/make_guess', methods=['POST'])
def make_guess():
    """Process a player's guess."""
    data = request.get_json()
    session_id = session.get('game_id')
    guess = data.get('guess', '').strip()
    
    if not session_id:
        return jsonify({'error': 'No active game session'}), 400
        
    result = game_manager.process_guess(session_id, guess)
    return jsonify(result)

@app.route('/get_hint', methods=['POST'])
def get_hint():
    """Get a hint for the current game."""
    session_id = session.get('game_id')
    
    if not session_id:
        return jsonify({'error': 'No active game session'}), 400
        
    result = game_manager.get_hint(session_id)
    return jsonify(result)

@app.route('/game_status')
def game_status():
    """Get current game status."""
    session_id = session.get('game_id')
    
    if not session_id:
        return jsonify({'error': 'No active game session'}), 400
        
    game_state = game_manager.get_game_state(session_id)
    if not game_state:
        return jsonify({'error': 'Game not found'}), 404
        
    elapsed_time = time.time() - game_state['start_time']
    time_remaining = max(0, game_state['time_limit'] - elapsed_time)
    
    # Check if time is up
    if time_remaining <= 0 and not game_state['game_over']:
        game_state['game_over'] = True
        
    return jsonify({
        'guesses_left': game_state['game'].guesses_left,
        'score': game_state['game'].player_score,
        'time_remaining': time_remaining,
        'game_over': game_state['game_over'],
        'won': game_state['won'],
        'guesses': game_state['guesses'],
        'target_combination': game_state['target_combination'] if game_state['game_over'] else None
    })

@app.route('/submit_score', methods=['POST'])
def submit_score():
    """Submit final score to leaderboard."""
    data = request.get_json()
    session_id = session.get('game_id')
    username = data.get('username', '').strip()
    
    if not session_id or not username:
        return jsonify({'error': 'Missing session or username'}), 400
        
    game_state = game_manager.get_game_state(session_id)
    if not game_state:
        return jsonify({'error': 'Game not found'}), 404
        
    # Add score to leaderboard
    final_score = game_state['game'].player_score
    rank, total = game_manager.score_manager.add_score(username, final_score)
    
    return jsonify({
        'success': True,
        'final_score': final_score,
        'rank': rank,
        'total_players': total
    })

@app.route('/leaderboard')
def leaderboard():
    """Get top 10 leaderboard."""
    top_scores = game_manager.score_manager.scores[:10]
    return jsonify({
        'leaderboard': [
            {
                'rank': i + 1,
                'username': entry['username'],
                'score': entry['score']
            }
            for i, entry in enumerate(top_scores)
        ]
    })

@app.route('/reset_game', methods=['POST'])
def reset_game():
    """Reset/end current game session."""
    session_id = session.get('game_id')
    
    if session_id and session_id in game_manager.active_games:
        del game_manager.active_games[session_id]
        
    session.pop('game_id', None)
    
    return jsonify({'success': True})

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    import os
    if not os.path.exists('templates'):
        os.makedirs('templates')
    if not os.path.exists('static'):
        os.makedirs('static')
        
    print("🎯 Starting Number Guessing Game Web Server...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    
    app.run(debug=True, host='0.0.0.0', port=5000)