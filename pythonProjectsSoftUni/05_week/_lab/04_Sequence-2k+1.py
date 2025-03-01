last_number = int(input())

number = 1
print(number)
while True:
    new_number = 2 * number + 1
    if new_number > last_number:
        break
    else:
        print(new_number)
        number = new_number
