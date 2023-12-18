import unittest
from days import day5
from days.day5 import obtain_seeds, obtain_maps, obtain_seed_ranges, apply_map
from utils.utils import block_parser


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = block_parser("data/example_day5.txt")
        expected_output = 35

        self.assertEqual(day5.solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = block_parser("data/day5.txt")
        expected_output = 313045984

        self.assertEqual(day5.solveA(input_data), expected_output)

    def test_example_2(self):
        input_data = block_parser("data/example_day5.txt")
        expected_output = 46

        self.assertEqual(day5.solveB(input_data), expected_output)

    def test_part_2(self):
        input_data = block_parser("data/day5.txt")
        expected_output = 20283860

        self.assertEqual(day5.solveB(input_data), expected_output)


class InternalFunctions(unittest.TestCase):
    def test_obtain_seeds(self):
        input_data = ["seeds: 79 14 55 13"]
        expected_output = [79, 14, 55, 13]
        result = obtain_seeds(input_data)
        self.assertEqual(result, expected_output)

    def test_obtain_maps(self):
        input_data = [
            "seeds: 79 14 55 13",
            "seed-to-soil map:\n50 98 2\n52 50 48",
            "soil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15",
            "fertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4",
            "water-to-light map:\n88 18 7\n18 25 70",
            "light-to-temperature map:\n45 77 23\n81 45 19\n68 64 13",
            "temperature-to-humidity map:\n0 69 1\n1 0 69",
            "humidity-to-location map:\n60 56 37\n56 93 4",
        ]

        expected_output = [
            [[50, 98, 2], [52, 50, 48]],
            [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
            [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
            [[88, 18, 7], [18, 25, 70]],
            [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
            [[0, 69, 1], [1, 0, 69]],
            [[60, 56, 37], [56, 93, 4]],
        ]
        result = obtain_maps(input_data)
        self.assertEqual(result, expected_output)

    def test_obtain_seed_ranges(self):
        input_data = ["seeds: 79 14 55 13"]
        expected_output = [(79, 93), (55, 68)]
        result = obtain_seed_ranges(input_data)
        self.assertEqual(result, expected_output)

    def test_apply_map(self):
        maps = [[10, 5, 3], [20, 15, 5], [35, 30, 2], [50, 40, 8]]
        seed = 5
        expected_output = 10
        result = apply_map(seed, maps)
        self.assertEqual(result, expected_output)

    def test_apply_map_with_no_matching_ranges(self):
        maps = [[10, 5, 3], [20, 15, 5], [35, 30, 2], [50, 40, 8]]
        step = 4
        expected_output = 4
        result = apply_map(step, maps)
        self.assertEqual(result, expected_output)
