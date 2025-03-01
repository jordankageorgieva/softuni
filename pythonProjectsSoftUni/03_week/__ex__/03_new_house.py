flower = input()
number_flower = int(input())
budget = float(input())

# "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus"

discount = 0
if flower ==  "Roses" and number_flower > 80:
    discount = 0.1
elif flower ==  "Dahlias" and number_flower > 90:
    discount = 0.15
elif flower ==  "Tulips" and number_flower > 80:
    discount = 0.15
elif (flower ==  "Narcissus") and (number_flower < 120):
    discount = -0.15
elif flower ==  "Gladiolus" and number_flower < 80:
    discount = -0.2

if flower ==  "Roses":
    money = number_flower * 5
elif flower == "Dahlias":
    money = number_flower * 3.80
elif flower == "Tulips":
    money = number_flower * 2.80
elif flower == "Narcissus":
    money = number_flower * 3
elif flower == "Gladiolus":
    money = number_flower * 2.50

if discount != 0:
    total_discount = (1 + ((-1) * discount))
    money = money * total_discount

if budget >= money:
    print(f"Hey, you have a great garden with {number_flower} {flower} and {budget - money:.02f} leva left.")
else:
    print(f"Not enough money, you need {money - budget:.02f} leva more.")