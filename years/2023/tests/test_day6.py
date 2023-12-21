import unittest
from days.day6 import (
    solveA,
    solveB,
    parse_input,
    calculate_critical_time,
    parse_input_bad_kerning,
)
from utils.utils import list_string_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        print(__name__)
        print("HERE")
        input_data = list_string_parser("data/example_day6.txt")
        expected_output = 288

        self.assertEqual(solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = list_string_parser("data/day6.txt")
        expected_output = 2269432

        self.assertEqual(solveA(input_data), expected_output)

    def test_example_2(self):
        input_data = list_string_parser("data/example_day6.txt")
        expected_output = 71503

        self.assertEqual(solveB(input_data), expected_output)

    def test_part_2(self):
        input_data = list_string_parser("data/day6.txt")
        expected_output = 35865985

        self.assertEqual(solveB(input_data), expected_output)


class InternalFunctions(unittest.TestCase):
    def test_parse_input(self):
        input_data = "Time:      7  15   30"
        actual_times = parse_input(input_data)
        expected_times = [7, 15, 30]
        self.assertEqual(expected_times, actual_times)

    def test_parse_input_bad_kerning(self):
        input_data = "Time:      7  15   30"
        actual_time = parse_input_bad_kerning(input_data)
        expected_time = 71530
        self.assertEqual(expected_time, actual_time)

    def test_critical_time(self):
        total_time = 10
        total_distance = 24
        expected_output = (5, 6)
        result = calculate_critical_time(total_time, total_distance)
        self.assertEqual(result, expected_output)
