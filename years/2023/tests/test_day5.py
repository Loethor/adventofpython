import unittest
from days import day5
from days.day5 import (
    Rules,
    ReverseRules,
    get_location,
)
from utils.utils import text_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = text_parser("data/example_day5.txt")
        expected_output = 35

        self.assertEqual(day5.solveA(input_data), expected_output)

    def test_part_1(self):
        # Write test cases based on expected functionality
        input_data = text_parser("data/day5.txt")
        expected_output = 313045984

        self.assertEqual(day5.solveA(input_data), expected_output)

    def test_example_2(self):
        # Write test cases based on expected functionality
        input_data = text_parser("data/example_day5.txt")
        expected_output = 46

        self.assertEqual(day5.solveB(input_data), expected_output)

    def test_part_2(self):
        # Write test cases based on expected functionality
        input_data = text_parser("data/day5.txt")
        expected_output = 20283860

        self.assertEqual(day5.solveB(input_data), expected_output)


class InternalFunctions(unittest.TestCase):
    def test_rules(self):
        input_str = "seed-to-soil map:\n50 98 2\n52 50 48"
        expected_rules = [[50, 98, 2], [52, 50, 48]]
        my_rules = Rules(input_str)
        self.assertEqual(my_rules.rules, expected_rules)

    def test_reverse_rules(self):
        input_str = "seed-to-soil map:\n50 98 2\n52 50 48"
        expected_rules = [[98, 50, 2], [50, 52, 48]]
        my_rules = ReverseRules(input_str)
        self.assertEqual(my_rules.rules, expected_rules)

    def test_apply_rules_in_range(self):
        input_str = "seed-to-soil map:\n50 98 2\n52 50 48"
        my_rules = Rules(input_str)
        expected_output = 50
        self.assertEqual(my_rules.apply_rules(98), expected_output)

    def test_apply_rules_out_range(self):
        input_str = "seed-to-soil map:\n50 98 2\n52 50 48"
        my_rules = Rules(input_str)
        expected_output = 30
        self.assertEqual(my_rules.apply_rules(30), expected_output)

    def test_get_location(self):
        seed_str = "seed-to-soil map:\n50 98 2"
        soil_str = "whatever-to-soil map:\n30 50 2"
        rules1 = Rules(seed_str)
        rules2 = Rules(soil_str)
        expected_output = 30

        self.assertEqual(get_location(98, [rules1, rules2]), expected_output)

    def test_apply_reverse_rules_in_range(self):
        input_str = "seed-to-soil map:\n50 98 2\n52 50 48"
        my_rules = ReverseRules(input_str)
        expected_output = 98
        self.assertEqual(my_rules.apply_rules(50), expected_output)

    def test_apply_rulesreverse__out_range(self):
        input_str = "seed-to-soil map:\n50 98 2\n52 50 48"
        my_rules = ReverseRules(input_str)
        expected_output = 30
        self.assertEqual(my_rules.apply_rules(30), expected_output)
