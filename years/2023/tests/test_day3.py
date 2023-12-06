import unittest
from days import day3
from utils.utils import naive_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = naive_parser("data/example_day3.txt")
        expected_output = 4361
        
        self.assertEqual(day3.solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = naive_parser("data/day3.txt")
        expected_output = 556057
        
        self.assertEqual(day3.solveA(input_data), expected_output)

    def test_example_2(self):
        # Write test cases based on expected functionality
        input_data = naive_parser("data/example_day3.txt")
        expected_output = 467835
        
        self.assertEqual(day3.solveB(input_data), expected_output)

    def test_part_2(self):
        # Write test cases based on expected functionality
        input_data = naive_parser("data/day3.txt")
        expected_output = 0
        
        self.assertEqual(day3.solveB(input_data), expected_output)