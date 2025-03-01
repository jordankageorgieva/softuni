name = input()

sum = 0
count = 1
negative_number = 0
while count <= 12:
    number = float(input())
    if number >= 4 and number <= 6:
        sum += number
        count += 1
    elif number < 4:
        negative_number += 1
        if negative_number == 2:
            print(f"{name} has been excluded at {count-1} grade")
            break
        count += 1

if negative_number < 1:
    average = sum / 12
    print(f"{name} graduated. Average grade: {average:.02f}")