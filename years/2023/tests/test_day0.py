import unittest
from days import day0

def naive_parser(file_name: str) -> [str]:
    with open(file_name, 'r') as file:
        data = file.read().splitlines()
    return data


class TestDay0(unittest.TestCase):
    def test_example_case(self):
        # Write test cases based on expected functionality
        input_data = naive_parser("data/example_day0.txt")
        expected_output = 24000
        
        self.assertEqual(day0.solve(input_data), expected_output)
        # Add more test cases as needed
