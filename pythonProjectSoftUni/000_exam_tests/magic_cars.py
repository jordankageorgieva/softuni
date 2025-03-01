import itertools

def generate_binary_permutations(n):
    # Generate all permutations of the string
    permutations = itertools.product('0123456789', repeat=n)

    # Convert permutations from tuples to strings
    perm_strings = [''.join(p) for p in permutations]

    return perm_strings

def generate_letter_permutations(n):
    # Generate all permutations of the string
    permutations = itertools.product('ABCEHKMPTX', repeat=n)

    # Convert permutations from tuples to strings
    perm_strings = [''.join(p) for p in permutations]

    return perm_strings


# pattern = "CAabcdXY"

magic_number = int(input())
n = 4
permutations_numbers = generate_binary_permutations(n)
print(permutations_numbers)
m = 2
permutations_letters = generate_letter_permutations(m)
print(permutations_letters)

iteration_number = 0
print(permutations_letters[len(permutations_letters)-1])


def is_magic_car_number(car_number):
    sum_numbers = 0
    for index_letter in range(len(car_number)):
        letter = car_number[index_letter]
        if letter == "A":
            sum_numbers += 10
        elif letter == "B":
            sum_numbers += 20
        elif letter == "C":
            sum_numbers += 30
        elif letter == "E":
            sum_numbers += 50
        elif letter == "H":
            sum_numbers += 80
        elif letter == "K":
            sum_numbers += 110
        elif letter == "M":
            sum_numbers += 130
        elif letter == "P":
            sum_numbers += 160
        elif letter == "T":
            sum_numbers += 200
        elif letter == "X":
            sum_numbers += 240
        elif letter.isdigit():
            sum_numbers += int(letter)

    return sum_numbers

count_magic_numbers= 0
while iteration_number < len(permutations_numbers):
    permutations_number = permutations_numbers[iteration_number]
    iteration_letter = 0
    while iteration_letter < len(permutations_letters):
        car_number = "CA" + permutations_number + permutations_letters[iteration_letter]
        sum_numbers = is_magic_car_number(car_number)
        # + is_magic_car_number(permutations_letters[iteration_letter])
        # sum_numbers_weight = sum(permutations_number)
        if sum_numbers == magic_number:
            print(f"car number {car_number} - sum number {sum_numbers}")
            count_magic_numbers += 1
        iteration_letter +=1
    iteration_number += 1

print(f"total magic numbers are {count_magic_numbers}")