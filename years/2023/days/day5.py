from typing import List


def solveA(input_data: [chr]) -> int:
    seeds = obtain_seeds(input_data)
    maps = obtain_maps(input_data)
    r = float("inf")

    for seed in seeds:
        for m in maps:
            seed = apply_map(seed, m)
        r = min(r, seed)

    print(r)
    return r


def solveB(input_data: [chr]) -> int:
    seeds = obtain_seed_ranges(input_data)
    maps = obtain_maps(input_data)
    for maps in maps:
        new_seeds = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            seeds = remap(start, end, new_seeds, maps, seeds)

        seeds = new_seeds

    print(min(seeds)[0])
    return min(seeds)[0]


def obtain_seeds(input_data):
    seeds = [int(x) for x in input_data[0].replace("seeds: ", "").split(" ")]
    return seeds


def obtain_maps(input_data):
    maps = [
        [[int(y) for y in x.split(" ")] for x in input_data[i].splitlines()[1::]]
        for i in range(1, 8)
    ]

    return maps


def apply_map(step: int, maps: List[List[int]]) -> int:
    for destination_range_start, source_range_start, range_length in maps:
        if step >= source_range_start and step < source_range_start + range_length:
            step = destination_range_start + (step - source_range_start)
            break

    return step


def obtain_seed_ranges(input_data):
    seed_input = [int(x) for x in input_data[0].replace("seeds: ", "").split(" ")]
    seeds = [
        (seed_input[i], seed_input[i] + seed_input[i + 1])
        for i in range(0, len(seed_input), 2)
    ]
    return seeds


def remap(
    start: int,
    end: int,
    new_seeds: list[tuple[int]],
    map: list[int],
    seeds: list[tuple[int]],
) -> int:
    for destination_range_start, source_range_start, range_length in map:
        overlap_start = max(start, source_range_start)
        overlap_end = min(end, source_range_start + range_length)

        if overlap_start < overlap_end:
            new_seeds.append(
                (
                    destination_range_start + (overlap_start - source_range_start),
                    destination_range_start + (overlap_end - source_range_start),
                )
            )

            if start < overlap_start:
                seeds.append((start, overlap_start))

            if overlap_end < end:
                seeds.append((overlap_end, end))

            break
    else:
        new_seeds.append((start, end))

    return seeds
