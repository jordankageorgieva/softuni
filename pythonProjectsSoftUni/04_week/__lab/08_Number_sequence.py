count= int(input())

max_number = 0
min_number = 0
for index in range(1, count + 1):
    number = int(input())
    if index == 1:
        max_number = number
        min_number = number

    if number > max_number:
        max_number = number

    if number < min_number:
        min_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")