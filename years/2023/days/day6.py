from typing import List
from functools import reduce

from utils.utils import timeit


@timeit
def solveA(input_data: List[str]) -> int:
    times = parse_input(input_data[0])
    distances = parse_input(input_data[1])

    victories = []
    for time, distance in zip(times, distances):
        victories.append(obtain_number_of_victories(time, distance))

    return reduce((lambda x, y: x * y), victories)


@timeit
def solveB(input_data: List[str]) -> int:
    time = parse_input_bad_kerning(input_data[0])
    distance = parse_input_bad_kerning(input_data[1])
    return obtain_number_of_victories2(time, distance)


def parse_input(input_data: str) -> List[int]:
    _, numbers = input_data.split(":")
    return list(map(int, numbers.strip().split()))


def obtain_number_of_victories(time: int, distance: int) -> int:
    victories = [1 for i in range(1, time) if (i * (time - i)) > distance]
    return sum(victories)


def obtain_number_of_victories2(time: int, distance: int) -> int:
    return sum(1 for i in range(1, time) if (i * (time - i)) > distance)


def parse_input_bad_kerning(input_data: str) -> int:
    _, numbers = input_data.split(":")
    return int(numbers.replace(" ", ""))
