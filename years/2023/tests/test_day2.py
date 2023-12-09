import unittest
from days import day2
from days.day2 import (
    process_game,
    process_set,
    verify_cubes,
    verify_games,
    find_minimum_cubes,
)
from utils.utils import naive_parser


class InternalFunctions(unittest.TestCase):
    def test_process_game(self):
        input_data = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        expected_id = 1
        expected_sets = [" 3 blue, 4 red", " 1 red, 2 green, 6 blue", " 2 green"]
        actual_id, actual_sets = process_game(input_data)
        self.assertEqual(expected_id, actual_id)
        self.assertEqual(expected_sets, actual_sets)

    def test_process_set_all_colors(self):
        input_set = "1 blue, 2 red, 3 green"
        expected_result = [1, 2, 3]
        self.assertEqual(process_set(input_set), expected_result)

    def test_process_set_missing_color(self):
        input_set = "1 blue, 2 red, 3 purple"
        with self.assertRaises(ValueError):
            process_set(input_set)

    def test_verify_cubes_valid_round(self):
        cubes = [12, 12, 13]
        self.assertTrue(verify_cubes(cubes))

    def test_verify_cubes_invalid_round(self):
        cubes = [15, 12, 13]
        self.assertFalse(verify_cubes(cubes))

    def test_verify_cubes_edge_case(self):
        cubes = [14, 12, 13]
        self.assertTrue(verify_cubes(cubes))

    def test_verify_games_all_valid_games(self):
        game_dict = {
            1: [True, True, True],
            2: [True, True, True],
            3: [True, True, True],
        }
        expected_games = 6
        self.assertEqual(verify_games(game_dict), expected_games)

    def test_verify_games_some_invalid_games(self):
        game_dict = {
            1: [True, True, True],
            2: [True, False, True],
            3: [True, True, True],
        }
        expected_games = 4

        self.assertEqual(verify_games(game_dict), expected_games)

    def test_verify_games_no_valid_games(self):
        game_dict = {
            1: [True, True, False],
            2: [True, False, True],
            3: [False, True, True],
        }
        self.assertEqual(verify_games(game_dict), 0)

    def test_same_id_same_cubes(self):
        games = [(1, [10, 15, 20]), (1, [5, 10, 25])]
        expected_result = {1: [10, 15, 25]}
        self.assertEqual(find_minimum_cubes(games), expected_result)

    def test_different_ids(self):
        games = [(1, [10, 15, 20]), (2, [5, 10, 25])]
        expected_result = {1: [10, 15, 20], 2: [5, 10, 25]}
        self.assertEqual(find_minimum_cubes(games), expected_result)

    def test_empty_input(self):
        games = []
        expected_result = {}
        self.assertEqual(find_minimum_cubes(games), expected_result)

    def test_single_game(self):
        games = [(1, [10, 15, 20])]
        expected_result = {1: [10, 15, 20]}
        self.assertEqual(find_minimum_cubes(games), expected_result)


class ExternalFunctions(unittest.TestCase):
    def test_example_1(self):
        input_data = naive_parser("data/example_day2.txt")
        expected_output = 8

        self.assertEqual(day2.solveA(input_data), expected_output)

    def test_part_1(self):
        input_data = naive_parser("data/day2.txt")
        expected_output = 2505

        self.assertEqual(day2.solveA(input_data), expected_output)

    def test_example_2(self):
        # Write test cases based on expected functionality
        input_data = naive_parser("data/example_day2.txt")
        expected_output = 2286

        self.assertEqual(day2.solveB(input_data), expected_output)

    def test_part_2(self):
        input_data = naive_parser("data/day2.txt")
        expected_output = 70265

        self.assertEqual(day2.solveB(input_data), expected_output)
