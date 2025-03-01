budget = float(input())
season = input()
number_fishers = int(input())

price = 0.0
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

discount = 0
if number_fishers <= 6:
    discount = 0.1
elif 7 < number_fishers <= 11:
    discount = 0.15
elif number_fishers > 12:
    discount = 0.25

extra_discount = 0
if number_fishers % 2 == 0 and season != "Autumn":
    extra_discount = 0.05

if discount != 0:
    total_discount = (1 -discount - extra_discount + discount * extra_discount)
    price = price * total_discount

if budget >= price:
    print(f"Yes! You have {budget - price:.02f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.02f} leva.")