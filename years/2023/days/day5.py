from typing import List


def solveA(input_data: [chr]) -> int:
    seeds, *map_strings = input_data.split("\n\n")
    seeds = list(map(int, seeds.split()[1:]))
    maps = [Rules(map_string) for map_string in map_strings]
    locations = []
    for seed in seeds:
        locations.append(get_location(seed, maps))
    return min(locations)


def solveB(input_data: [chr]) -> int:
    seeds, *map_strings = input_data.split("\n\n")
    seeds = list(map(int, seeds.split()[1:]))

    ranges_of_seeds: List[RangePair] = []
    for i in range(0, len(seeds), 2):
        ranges_of_seeds.append(RangePair(seeds[i], seeds[i] + seeds[i + 1]))

    reverse_maps = [ReverseRules(map_string) for map_string in map_strings]

    sol = None
    location = 0
    while sol is None:
        seed = get_seed(location, reverse_maps)
        for rng in ranges_of_seeds:
            if rng.is_value_contained(seed):
                sol = location
                break
        location += 1
    return sol


class Rules:
    def __init__(self, map_string) -> None:
        self.rules = []
        for line in map_string.splitlines()[1:]:
            dst, src, rng = map(int, line.split())
            self.rules.append([dst, src, rng])

    def apply_rules(self, key):
        for dst, src, rng in self.rules:
            if src <= key < src + rng:
                return dst + key - src
        return key


class RangePair:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def is_value_contained(self, value: int) -> bool:
        return self.lower <= value < self.upper


class ReverseRules:
    def __init__(self, map_string) -> None:
        self.rules = []
        for line in map_string.splitlines()[1:]:
            dst, src, rng = map(int, line.split())
            self.rules.append([src, dst, rng])

    def apply_rules(self, key):
        for dst, src, rng in self.rules:
            if src <= key < src + rng:
                return dst + key - src
        return key


def get_location(seed, rules: List[Rules]):
    for rule in rules:
        seed = rule.apply_rules(seed)
    return seed


def get_seed(location, rules: List[Rules]):
    for rule in reversed(rules):
        location = rule.apply_rules(location)
    return location
