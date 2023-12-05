# import unittest
# from days import day1

# def naive_parser(file_name: str) -> [str]:
#     with open(file_name, 'r') as file:
#         data = file.read().splitlines()
#     return data


# class TestDay1(unittest.TestCase):
#     def test_example_1(self):
#         # Write test cases based on expected functionality
#         input_data = naive_parser("data/example_day1A.txt")
#         expected_output = 142
        
#         self.assertEqual(day1.solveA(input_data), expected_output)

#     def test_part_1(self):
#         # Write test cases based on expected functionality
#         input_data = naive_parser("data/day1.txt")
#         expected_output = 55488
        
#         self.assertEqual(day1.solveA(input_data), expected_output)

#     def test_example_2(self):
#         # Write test cases based on expected functionality
#         input_data = naive_parser("data/example_day1B.txt")
#         expected_output = 281+77
        
#         self.assertEqual(day1.solveB(input_data), expected_output)

#     def test_part_2(self):
#         # Write test cases based on expected functionality
#         input_data = naive_parser("data/day1.txt")
#         expected_output = 0
        
#         self.assertEqual(day1.solveB(input_data), expected_output)