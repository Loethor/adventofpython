from functools import wraps
import time


def list_string_parser(file_name: str) -> [str]:
    with open(file_name, "r") as file:
        data = file.read().splitlines()
    return data


def text_parser(file_name: str) -> [str]:
    with open(file_name, "r") as file:
        data = file.read()
    return data


def block_parser(file_name: str) -> [str]:
    with open(file_name, "r") as file:
        data = file.read()
        blocks = [block.strip() for block in data.split("\n\n") if block.strip()]
        return blocks


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"{func.__name__} took {total_time:.4f} seconds")
        return result

    return timeit_wrapper
