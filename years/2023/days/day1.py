from utils.utils import timeit


@timeit
def solveA(input_data: [chr]) -> int:
    first_number = ""
    second_number = ""
    sum = 0
    for word in input_data:
        for character in word:
            if character.isnumeric():
                if first_number == "":
                    first_number = character
                    second_number = character
                else:
                    second_number = character
        sum += int(first_number + second_number)
        first_number = ""
        second_number = ""
    return sum


@timeit
def solveB(input_data: [chr]) -> int:
    first_number = ""
    second_number = ""
    word2number = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    sum = 0
    hits = []
    for word in input_data:
        for key in word2number.keys():
            if key in word:
                start_index = word.index(key)
                last_index = word.rindex(key)
                hits.append((start_index, word2number[key]))
                hits.append((last_index, word2number[key]))
        for character in word:
            if character.isnumeric():
                start_index = word.index(character)
                last_index = word.rindex(character)
                hits.append((start_index, character))
                hits.append((last_index, character))
        min_index = 999999999
        max_index = -1
        for pair in hits:
            if pair[0] < min_index:
                min_index = pair[0]
                first_number = pair[1]
            if pair[0] > max_index:
                max_index = pair[0]
                second_number = pair[1]
        hits = []
        sum += int(first_number + second_number)
    return sum
