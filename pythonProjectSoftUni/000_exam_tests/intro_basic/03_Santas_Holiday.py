days = int(input())
room = input()
grade = input()

nights = days - 1
discount = 0
# print(room)
if room == "room for one person":
    money_per_night = 18
    money = nights * money_per_night
    if grade == "positive":
        money += money * 25 / 100
        print(f"{money:.2f}")
    elif grade == "negative":
        money -= money * 10 / 100
        print(f"{money:.2f}")

elif room == "apartment":
    money_per_night = 25
    money = nights * money_per_night
    if days <= 10:
        discount = 30
        money -= money * discount / 100
        if grade == "positive":
            money += money * 25 / 100
            print(f"{money:.2f}")
        elif grade == "negative":
            money -= money * 10 / 100
            print(f"{money:.2f}")
    elif 10 < days < 15:
        discount = 35
        money -= money * discount/100
        if grade == "positive":
            money += money * 25/100
            print(f"{money:.2f}")
        elif grade == "negative":
            money -= money * 10/100
            print(f"{money:.2f}")
    elif days >= 15:
        discount = 50
        money -= money * discount / 100
        if grade == "positive":
            money += money * 25 / 100
            print(f"{money:.2f}")
        elif grade == "negative":
            money -= money * 10 / 100
            print(f"{money:.2f}")
elif room == "president apartment":
    money_per_night = 35
    money = nights * money_per_night
    if days <= 10:
        discount = 10
        money -= money * discount / 100
        if grade == "positive":
            money += money * 25 / 100
            print(f"{money:.2f}")
        elif grade == "negative":
            money -= money * 10 / 100
            print(f"{money:.2f}")
    elif 10 < days < 15:
        discount = 15
        money -= money * discount / 100
        if grade == "positive":
            money += money * 25 / 100
            print(f"{money:.2f}")
        elif grade == "negative":
            money -= money * 10 / 100
            print(f"{money:.2f}")
    elif days >= 15:
        discount = 20
        money -= money * discount / 100
        if grade == "positive":
            money += money * 25 / 100
            print(f"{money:.2f}")
        elif grade == "negative":
            money -= money * 10 / 100
            print(f"{money:.2f}")
