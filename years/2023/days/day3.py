def solveA(input_data: [chr]) -> int:
    numbers = []
    symbols = []
    start = None

    for j, line in enumerate(input_data):
        for i, char in enumerate(line):
            if not char.isdigit() and char != ".":
                symbols.append([j, i])

            if char.isdigit():
                if start is None:
                    start = i
            elif start is not None:
                numbers.append([j, int(line[start:i]), start, i - 1])
                start = None

        # Check if there's an unfinished number at the end of the string
        if start is not None:
            numbers.append([j, int(line[start:]), start, len(line) - 1])
            start = None

    sol = []
    for number in numbers:
        found = False
        for symbol in symbols:
            if found:
                break
            y1 = number[0]
            x1_list = [x for x in range(number[2], number[3] + 1, 1)]
            y2 = symbol[0]
            x2 = symbol[1]
            if abs(y2 - y1) > 1:
                continue
            for x1 in x1_list:
                if chebyshev_distance(x1, y1, x2, y2) <= 1:
                    sol.append(number[1])
                    found = True
                    break
    return sum(sol)


def solveB(input_data: [chr]) -> int:
    numbers = []
    symbols = []
    start = None

    for j, line in enumerate(input_data):
        for i, char in enumerate(line):
            if char == "*":
                symbols.append([j, i])

            if char.isdigit():
                if start is None:
                    start = i
            elif start is not None:
                numbers.append([j, int(line[start:i]), start, i - 1])
                start = None

        # Check if there's an unfinished number at the end of the string
        if start is not None:
            numbers.append([j, int(line[start:]), start, len(line) - 1])
            start = None

    sol_dict = {}
    for i, symbol in enumerate(symbols):
        for number in numbers:
            y1 = number[0]
            x1_list = [x for x in range(number[2], number[3] + 1, 1)]
            y2 = symbol[0]
            x2 = symbol[1]
            for x1 in x1_list:
                if chebyshev_distance(x1, y1, x2, y2) <= 1:
                    sol_dict.setdefault(i, []).append(number[1])
                    break
    sol = 0
    for number_list in sol_dict.values():
        if len(number_list) == 2:
            sol += number_list[0] * number_list[1]
    return sol


def chebyshev_distance(x1, y1, x2, y2):
    return max(abs(x2 - x1), abs(y2 - y1))
