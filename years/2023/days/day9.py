from typing import List
from utils.utils import timeit


@timeit
def solveA(input_data: List[str]) -> int:
    element = 0
    for sequence in input_data:
        sequence_int = [int(element) for element in sequence.split()]
        element += calculate_last_element(sequence_int)
    return element


@timeit
def solveB(input_data: List[str]) -> int:
    element = 0
    for sequence in input_data:
        sequence_int = [int(element) for element in sequence.split()]
        element += calculate_first_element(sequence_int)
    return element


def calculate_last_element(sequence: List[int]) -> int:
    diff_sequence = calculate_diff_sequence(sequence)
    element = 0
    if diff_sequence != [0] * len(diff_sequence):
        element = calculate_last_element(diff_sequence)
        element += sequence[-1]
    else:
        element = sequence[-1] + diff_sequence[-1]
    return element


def calculate_diff_sequence(sequence: List[int]) -> List[int]:
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]


def calculate_first_element(sequence: List[int]) -> int:
    diff_sequence = calculate_diff_sequence(sequence)
    element = 0
    if diff_sequence != [0] * len(diff_sequence):
        element = calculate_first_element(diff_sequence)
        element = sequence[0] - element
    else:
        element = sequence[0] + diff_sequence[0]
    return element
