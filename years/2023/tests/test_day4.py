import unittest
from days import day4
from utils.utils import naive_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = naive_parser("data/example_day4.txt")
        expected_output = 13

        self.assertEqual(day4.solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = naive_parser("data/day4.txt")
        expected_output = 24160

        self.assertEqual(day4.solveA(input_data), expected_output)

    def test_example_2(self):
        input_data = naive_parser("data/example_day4.txt")
        expected_output = 30

        self.assertEqual(day4.solveB(input_data), expected_output)

    def test_part_2(self):
        input_data = naive_parser("data/day4.txt")
        expected_output = 5659035

        self.assertEqual(day4.solveB(input_data), expected_output)
