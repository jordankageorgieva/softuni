from itertools import product

patterns = ["aaaa", "abbb", "aaab", "aabb", "abab", "abba"]


def generate_car_numbers(pattern):
    unique_digits = list(range(10))  # Digits 0-9
    results = set()

    for digits in product(unique_digits, repeat=len(set(pattern))):
        mapping = dict(zip(sorted(set(pattern)), digits))
        results.add("".join(str(mapping[ch]) for ch in pattern))

    return sorted(results)

def generate_letter_permutations(n):
    # Generate all permutations of the string
    permutations = product('ABCEHKMPTX', repeat=n)

    # Convert permutations from tuples to strings
    perm_strings = [''.join(p) for p in permutations]

    return perm_strings

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

m = 2
permutations_letters = generate_letter_permutations(m)
print(permutations_letters)

count_magic_numbers = 0
# Generate and print results
for index in patterns:
    print(f"Pattern: {index}")
    car_numbers = generate_car_numbers(index)
    print(car_numbers)
    # iteration_letter = 0
    # while iteration_letter < len(car_numbers):
    #     car_number = "CA" + car_numbers[index] + permutations_letters[iteration_letter]
    #     sum_numbers = is_magic_car_number(car_number)
    #     print(f"car number {car_number} - sum number {sum_numbers}")
    #     # + is_magic_car_number(permutations_letters[iteration_letter])
    #     # sum_numbers_weight = sum(permutations_number)
    #     # if sum_numbers == magic_number:
    #     #     print(f"car number {car_number} - sum number {sum_numbers}")
    #     #     count_magic_numbers += 1
    #     iteration_letter += 1


