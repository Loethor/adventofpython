from typing import List
from functools import reduce


def solveA(input_data: [chr]) -> int:
    games = []
    for line in input_data:
        (id, sets) = process_game(line)      
        for set in sets:
            cubes = process_set(set)
            games.append([id, cubes])
            
    game_dict = {}
    for id, cubes in games:
        is_valid = verify_cubes(cubes)
        game_dict.setdefault(id, []).append(is_valid)
    
    solution = verify_games(game_dict)
    return solution

def solveB(input_data: [chr]) -> int:
    games = []
    for line in input_data:
        (id, sets) = process_game(line)      
        for set in sets:
            cubes = process_set(set)
            games.append([id, cubes])
            
    game_dict = find_minimum_cubes(games)
    
    solution = 0
    for cubes in game_dict.values():
        solution += reduce(lambda x, y: x * y, cubes, 1)

    return solution

def find_minimum_cubes(games):
    game_dict = {}
    for id, cubes in games:
        if id in game_dict:
            old = game_dict[id].copy() # paranoid
            game_dict[id] = [max(x,y) for x,y in zip(cubes, old)]
        else:
            game_dict[id] = cubes
    return game_dict

def process_game(line: str) -> (int, List[str]):
    rounds = line.split(":")
    game_id = rounds[0].split(" ")
    id = int(game_id[1])
    sets = rounds[1].split(";")
    return (id, sets)

def process_set(set):
    parts = set.split(",")
    balls = [0,0,0]
    for part in parts:
        num, color = part.split()
        num = int(num)
        match color:
            case 'blue':
                balls[0] = num
            case 'red':
                balls[1] = num
            case 'green':
                balls[2] = num
            case _:
                raise ValueError("That color is not expected.")
    return balls

def verify_cubes(cubes: List[int]) -> bool:
    #only 12 red cubes, 13 green cubes, and 14 blue cubes
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14
    valid_threshold = [blue_cubes, red_cubes, green_cubes]
    is_valid = False
    if all( x <= y for x,y in zip(cubes, valid_threshold)):
        is_valid = True
    return is_valid

def verify_games(game_dict):
    total_sum = 0
    for game_id, cubes in game_dict.items():
        if all(cubes):
            total_sum += game_id
    return total_sum