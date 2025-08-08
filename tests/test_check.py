"""
Author: DG
Version: 2.0
Date: August 2025
Purpose: This file test the check.py file using unit test "
"""

import unittest
import sys
import os


# Add the parent directory to the path to import modules
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
backend_dir = os.path.join(project_root, 'backend')
sys.path.insert(0, backend_dir)

from check import Checker


class TestChecker(unittest.TestCase):
    """
    Test cases for the Checker class - the core feedback mechanism.
    
    This class is critical as it determines the accuracy of game feedback,
    which is essential for proper gameplay experience.
    """

    def test_all_digits_correct_and_correct_location(self):
        target = [1, 2, 3, 4]
        guess = [1, 2, 3, 4]
        checker = Checker(user_guess_digits=guess, target_digits=target)
        total_correct, correct_location, message = checker.feedback_provider()

        self.assertEqual(total_correct, 4)
        self.assertEqual(correct_location, 4)
        self.assertIn("4 correct number and 4 correct location", message)

    def test_all_digits_incorrect(self):
        target = [1, 2, 3, 4]
        guess = [5, 6, 7, 8]
        checker = Checker(user_guess_digits=guess, target_digits=target)
        total_correct, correct_location, message = checker.feedback_provider()

        self.assertEqual(total_correct, 0)
        self.assertEqual(correct_location, 0)
        self.assertEqual(message, "All digits are incorrect")

    def test_correct_digits_wrong_positions(self):
        target = [1, 2, 3, 4]
        guess = [4, 3, 2, 1]
        checker = Checker(user_guess_digits=guess, target_digits=target)
        total_correct, correct_location, message = checker.feedback_provider()

        self.assertEqual(total_correct, 4)
        self.assertEqual(correct_location, 0)
        self.assertIn("4 correct number and 0 correct location", message)

    def test_mixed_correct_and_wrong_positions(self):
        target = [1, 2, 3, 4]
        guess = [1, 4, 2, 5]
        checker = Checker(user_guess_digits=guess, target_digits=target)
        total_correct, correct_location, message = checker.feedback_provider()

        self.assertEqual(total_correct, 3)
        self.assertEqual(correct_location, 1)
        self.assertIn("3 correct number and 1 correct location", message)

    def test_correct_combination_true(self):
        target = [1, 2, 3, 4]
        guess = [1, 2, 3, 4]
        checker = Checker(user_guess_digits=guess, target_digits=target)
        self.assertTrue(checker.correct_combination())

    def test_correct_combination_false(self):
        target = [1, 2, 3, 4]
        guess = [4, 3, 2, 1]
        checker = Checker(user_guess_digits=guess, target_digits=target)
        self.assertFalse(checker.correct_combination())

if __name__ == "__main__":
    unittest.main()