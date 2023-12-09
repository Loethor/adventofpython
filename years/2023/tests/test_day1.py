import unittest
from days import day1
from utils.utils import naive_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = naive_parser("data/example_day1A.txt")
        expected_output = 141
        
        self.assertEqual(day1.solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = naive_parser("data/day1.txt")
        expected_output = 55488
        
        self.assertEqual(day1.solveA(input_data), expected_output)

    def test_example_2(self):
        input_data = naive_parser("data/example_day1B.txt")
        expected_output = 281
        
        self.assertEqual(day1.solveB(input_data), expected_output)

    def test_part_2(self):
        input_data = naive_parser("data/day1.txt")
        expected_output = 55614
        
        self.assertEqual(day1.solveB(input_data), expected_output)