import unittest
from days.day4 import (
    solveA,
    solveB,
)
from utils.utils import list_string_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = list_string_parser("data/example_day4.txt")
        expected_output = 13

        self.assertEqual(solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = list_string_parser("data/day4.txt")
        expected_output = 24160

        self.assertEqual(solveA(input_data), expected_output)

    def test_example_2(self):
        input_data = list_string_parser("data/example_day4.txt")
        expected_output = 30

        self.assertEqual(solveB(input_data), expected_output)

    def test_part_2(self):
        input_data = list_string_parser("data/day4.txt")
        expected_output = 5659035

        self.assertEqual(solveB(input_data), expected_output)
