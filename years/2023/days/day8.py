from typing import List, Dict
from utils.utils import timeit
from math import lcm

Nodes = Dict[str, List[str]]


@timeit
def solveA(input_data: List[str]) -> int:
    instructions: str = input_data[0]
    nodes = obtain_nodes(input_data)
    return obtain_steps("AAA", "ZZZ", instructions, nodes)


@timeit
def solveB(input_data: List[str]) -> int:
    instructions = input_data[0]
    nodes = obtain_nodes(input_data)
    return obtain_ghost_steps(instructions, nodes)


def obtain_nodes(input_data: List[str]) -> Nodes:
    nodes_str: str = input_data[1]
    nodes = {}
    for node in nodes_str.split("\n"):
        key, values = node.split(" = ")
        values = values.replace("(", "")
        values = values.replace(")", "")
        subnodes = values.split(", ")
        nodes[key] = subnodes
    return nodes


def obtain_steps(starting_node, condition, instructions: str, nodes: Nodes) -> int:
    cycled_index = 0
    steps = 0
    while not starting_node.endswith(condition):
        my_instruction = instructions[cycled_index]
        match my_instruction:
            case "R":
                starting_node = nodes[starting_node][1]
            case "L":
                starting_node = nodes[starting_node][0]
            case _:  # unreachable
                return -1
        cycled_index = (cycled_index + 1) % len(instructions)
        steps += 1
    return steps


def obtain_ghost_steps(instructions: str, nodes: Nodes) -> int:
    starting_nodes: List[str] = [node for node in nodes.keys() if node.endswith("A")]
    list_of_steps: List[int] = []
    for starting_node in starting_nodes:
        list_of_steps.append(obtain_steps(starting_node, "Z", instructions, nodes))
    return lcm(*list_of_steps)
