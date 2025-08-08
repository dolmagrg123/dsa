import unittest
import sys
import os
from unittest.mock import patch, MagicMock

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
backend_dir = os.path.join(project_root, 'backend')
sys.path.insert(0, backend_dir)
from game import Game

class TestGameInitialization(unittest.TestCase):
    def test_game_initialization(self):
        length = 4
        min_val = 1
        max_val = 6
        target = [1, 2, 3, 4]
        
        game = Game(length, min_val, max_val, target)
        
        self.assertEqual(game.length, length)
        self.assertEqual(game.min_val, min_val)
        self.assertEqual(game.max_val, max_val)
        self.assertEqual(game.target_combination, target)
        self.assertEqual(game.guesses_left, 10)
        self.assertEqual(game.player_score, 0)
        self.assertEqual(game.hinted_positions, set())

class TestGameHintBehavior(unittest.TestCase):

    @patch('builtins.input', side_effect=(x for x in ['y', 'n'] + ['n'] * 10)) # takes only one hint, n to all other times
    def test_hint_reduces_score_and_skips_guess(self, mock_input):
        length = 4
        min_val = 1
        max_val = 6
        target = [1, 2, 3, 4]

        game = Game(length, min_val, max_val, target)

        game.input_validator.input_validator = MagicMock(return_value=[0,0,0,0])
        game.guesses_left = 2

        final_score = game.game_plan()

        self.assertEqual(final_score, 0)
        self.assertEqual(len(game.hinted_positions), 1)
        self.assertTrue(all(pos in range(length) for pos in game.hinted_positions))

class TestGameWinCondition(unittest.TestCase):
    @patch('builtins.input', side_effect=(x for x in ['n']))  # No hint, just guess
    @patch('builtins.print')  # Mock print to suppress output or check messages if needed
    def test_game_win_on_first_guess(self, mock_print, mock_input):
        length = 4
        min_val = 1
        max_val = 6
        target = [1, 2, 3, 4]

        game = Game(length, min_val, max_val, target)

        # Mock input_validator to always return the correct guess on first try
        game.input_validator.input_validator = MagicMock(return_value=target)
        game.guesses_left = 10

        final_score = game.game_plan()

        # Correct digits and locations = 4 + 4 = 8 points added
        # Bonus = guesses_left * 10 * length
        # Guesses left decreases by 1 after guess, so guesses_left = 9 at bonus time
        expected_score = 8 + 9 * 10 * length  # 8 + 9*10*4 = 8 + 360 = 368

        self.assertEqual(final_score, expected_score)

        # Check that the winning message was printed
        # It should include "Congratulations" in some print call
        printed_texts = [args[0] for args, _ in mock_print.call_args_list]
        self.assertTrue(any("Congratulations" in text for text in printed_texts))


if __name__ == "__main__":
    unittest.main()
