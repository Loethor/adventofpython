def solveA(input_data: [chr]) -> int:
    sum = 0
    for line in input_data:
        _ , numbers = line.split(":")
        winning_numbers, my_numbers = numbers.split("|")
        winning_numbers = set(int(num) for num in winning_numbers.split() if num.strip())
        my_numbers = set(int(num) for num in my_numbers.split() if num.strip())

        prize = len(winning_numbers.intersection(my_numbers))
        if prize > 0:
           sum += 2**(prize-1)

    return sum

def solveB(input_data: [chr]) -> int:
    copies = [1]*len(input_data)
    for i,line in enumerate(input_data):
        _, numbers = line.split(":")
        winning_numbers, my_numbers = numbers.split("|")
        winning_numbers = set(int(num) for num in winning_numbers.split() if num.strip())
        my_numbers = set(int(num) for num in my_numbers.split() if num.strip())

        prize = len(winning_numbers.intersection(my_numbers))
        for j in range(prize):
            copies[j+i+1] = copies[j+i+1] + copies[i] 
    return sum(copies)