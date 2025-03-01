import sys

number = int(input())

max_number = -sys.maxsize
sum = 0
sum_other_numbers= 0

for _ in range(number):
    input_num = int(input())

    if input_num > max_number:
        max_number = input_num

    sum += input_num

if max_number == sum - max_number:
    print("Yes")
    print(f"Sum = {sum - max_number}")
else:
    print("No")
    sum_other_numbers = sum - max_number
    print(f"Diff = {abs(max_number - sum_other_numbers)} ")
