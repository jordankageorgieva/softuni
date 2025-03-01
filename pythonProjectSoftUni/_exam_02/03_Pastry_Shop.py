type_cake= input()
num_cakes = int(input())
day_december = int(input())

if type_cake == "Cake":
    if day_december <= 15:
        money = num_cakes * 24
    elif day_december > 15:
        money = num_cakes * 28.7

    if day_december <= 22:
        if 100 <= money <= 200:
            money -= money * 0.15
        elif money > 200:
            money -= money * 0.25

        if day_december <= 15:
            money -= money * 0.1
elif type_cake == "Souffle":
    if day_december <= 15:
        money = num_cakes * 6.66
    elif day_december > 15:
        money = num_cakes * 9.8

    if day_december <= 22:
        if 100 <= money <= 200:
            money -= money * 0.15
        elif money > 200:
            money -= money * 0.25

        if day_december <= 15:
            money -= money * 0.1

elif type_cake == "Baklava":
    if day_december <= 15:
        money = num_cakes * 12.60
    elif day_december > 15:
        money = num_cakes * 16.98

    if day_december <= 22:
        if 100 <= money <= 200:
            money -= money * 0.15
        elif money > 200:
            money -= money * 0.25

        if day_december <= 15:
            money -= money * 0.1

print(f"{money:.02f}")
