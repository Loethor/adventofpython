import unittest
from days import day6
from days.day6 import (
    parse_input,
    obtain_number_of_victories,
    parse_input_bad_kerning,
)
from utils.utils import list_string_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = list_string_parser("data/example_day6.txt")
        expected_output = 288

        self.assertEqual(day6.solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = list_string_parser("data/day6.txt")
        expected_output = 2269432

        self.assertEqual(day6.solveA(input_data), expected_output)

    def test_example_2(self):
        input_data = list_string_parser("data/example_day6.txt")
        expected_output = 71503

        self.assertEqual(day6.solveB(input_data), expected_output)

    def test_part_2(self):
        input_data = list_string_parser("data/day6.txt")
        expected_output = 35865985

        self.assertEqual(day6.solveB(input_data), expected_output)


class InternalFunctions(unittest.TestCase):
    def test_parse_input(self):
        input_data = "Time:      7  15   30"
        actual_times = parse_input(input_data)
        expected_times = [7, 15, 30]
        self.assertEqual(expected_times, actual_times)

    def test_obtain_number_of_victories(self):
        time = 7
        distance = 9
        actual_victories = obtain_number_of_victories(time, distance)
        expected_victories = 4
        self.assertEqual(actual_victories, expected_victories)

    def test_parse_input_bad_kerning(self):
        input_data = "Time:      7  15   30"
        actual_time = parse_input_bad_kerning(input_data)
        expected_time = 71530
        self.assertEqual(expected_time, actual_time)
