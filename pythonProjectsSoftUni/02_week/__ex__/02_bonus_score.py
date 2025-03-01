number = int(input())

bonus = 0
if number < 100:
    bonus = 5
elif number >= 100 and number <= 1000:
    bonus = bonus + number * 20/100
elif number > 1000:
    bonus = bonus + number * 10/100


additional_bonus = 0
if number % 2 == 0:
    additional_bonus = 1
# if str(number)[-1] == '5':
#     additional_bonus = 2
if number % 10 == 5:
    additional_bonus = 2

total_bonus = bonus + additional_bonus
total = number + total_bonus
print(total_bonus)
print(total)