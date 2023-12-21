import unittest
from days import day8

from utils.utils import block_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = block_parser("data/example_day8A.txt")
        expected_output = 6

        self.assertEqual(day8.solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = block_parser("data/day8.txt")
        expected_output = 20569

        self.assertEqual(day8.solveA(input_data), expected_output)

    def test_example_2(self):
        input_data = block_parser("data/example_day8B.txt")
        expected_output = 6

        self.assertEqual(day8.solveB(input_data), expected_output)

    def test_part_2(self):
        input_data = block_parser("data/day8.txt")
        expected_output = 21366921060721

        self.assertEqual(day8.solveB(input_data), expected_output)
