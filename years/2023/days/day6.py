from typing import List

from utils.utils import timeit
from math import floor, sqrt


@timeit
def solveA(input_data: List[str]) -> int:
    times = parse_input(input_data[0])
    distances = parse_input(input_data[1])
    product_of_victories = 1
    for time, distance in zip(times, distances):
        cl, ch = calculate_critical_time(time, distance)
        product_of_victories *= len(range(cl, ch))
    return product_of_victories


@timeit
def solveB(input_data: List[str]) -> int:
    time = parse_input_bad_kerning(input_data[0])
    distance = parse_input_bad_kerning(input_data[1])
    cl, ch = calculate_critical_time(time, distance)
    return len(range(cl, ch))


def parse_input(input_data: str) -> List[int]:
    _, numbers = input_data.split(":")
    return list(map(int, numbers.strip().split()))


def parse_input_bad_kerning(input_data: str) -> int:
    _, numbers = input_data.split(":")
    return int(numbers.replace(" ", ""))


def calculate_critical_time(total_time: int, total_distance: int):
    # solution of the quadratic formula
    time_squared = total_time * total_time
    factor = sqrt(time_squared - 4 * total_distance)

    critical_low = (total_time - factor) / 2
    critical_high = (total_time + factor) / 2

    # if critical_high whole number
    if floor(critical_high) == critical_high:
        return floor(critical_low) + 1, floor(critical_high)
    else:
        return floor(critical_low) + 1, floor(critical_high) + 1
