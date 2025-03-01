month = input()
number_nights = int(input())

money_studio = 0.0
money_apartment = 0.0
if month == 'May' or month == 'October':
    money_studio = number_nights * 50.00
    money_apartment = number_nights * 65.00
    if 7 < number_nights < 14:
        money_studio = money_studio * (1 - 0.05)
    elif number_nights >= 14:
        money_studio = money_studio * (1 - 0.3)
        money_apartment = money_apartment * (1 - 0.1)
elif month == 'June' or month == 'September':
    money_studio = number_nights * 75.20
    money_apartment = number_nights * 68.70
    if number_nights > 14:
        money_studio = money_studio * (1 - 0.2)
        money_apartment = money_apartment * (1 - 0.1)
elif month == 'July' or month == 'August':
    money_studio = number_nights * 76.00
    money_apartment = number_nights * 77.00
    if number_nights > 14:
        money_apartment = money_apartment * (1 - 0.1)

print(f'Apartment: {money_apartment:.02f} lv.')
print(f'Studio: {money_studio:.02f} lv.')