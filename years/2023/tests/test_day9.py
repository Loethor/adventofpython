import unittest
from days.day9 import solveA, solveB

from utils.utils import list_string_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = list_string_parser("data/example_day9.txt")
        expected_output = 114

        self.assertEqual(solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = list_string_parser("data/day9.txt")
        expected_output = 1806615041

        self.assertEqual(solveA(input_data), expected_output)

    def test_example_2(self):
        input_data = list_string_parser("data/example_day9.txt")
        expected_output = 2

        self.assertEqual(solveB(input_data), expected_output)

    def test_part_2(self):
        input_data = list_string_parser("data/day9.txt")
        expected_output = 1211

        self.assertEqual(solveB(input_data), expected_output)
