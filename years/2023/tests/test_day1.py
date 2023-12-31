import unittest
from days.day1 import solveA, solveB
from utils.utils import list_string_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = list_string_parser("data/example_day1A.txt")
        expected_output = 142

        self.assertEqual(solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = list_string_parser("data/day1.txt")
        expected_output = 55488

        self.assertEqual(solveA(input_data), expected_output)

    def test_example_2(self):
        input_data = list_string_parser("data/example_day1B.txt")
        expected_output = 281

        self.assertEqual(solveB(input_data), expected_output)

    def test_part_2(self):
        input_data = list_string_parser("data/day1.txt")
        expected_output = 55614

        self.assertEqual(solveB(input_data), expected_output)
