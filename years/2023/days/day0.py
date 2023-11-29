def solve(input_data: [chr]) -> int:
    elves = []

    print(input_data)

    current_elf_load = 0
    for element in input_data:
        if element == '':
            elves.append(current_elf_load)
            current_elf_load = 0
        else:
            current_elf_load += int(element)

    # Your solution for day 1
    return max(elves)
