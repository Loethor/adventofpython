import unittest
from days.day3 import (
    solveA,
    solveB,
)
from utils.utils import list_string_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = list_string_parser("data/example_day3.txt")
        expected_output = 4361

        self.assertEqual(solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = list_string_parser("data/day3.txt")
        expected_output = 556057

        self.assertEqual(solveA(input_data), expected_output)

    def test_example_2(self):
        # Write test cases based on expected functionality
        input_data = list_string_parser("data/example_day3.txt")
        expected_output = 467835

        self.assertEqual(solveB(input_data), expected_output)

    def test_part_2(self):
        # Write test cases based on expected functionality
        input_data = list_string_parser("data/day3.txt")
        expected_output = 82824352

        self.assertEqual(solveB(input_data), expected_output)
