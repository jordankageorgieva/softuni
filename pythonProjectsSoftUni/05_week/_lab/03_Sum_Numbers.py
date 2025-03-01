sum_number = int(input())

sum_new_numbers = 0
while True:
    number = int(input())
    sum_new_numbers += number
    if sum_new_numbers >= sum_number:
        print(sum_new_numbers)
        break
