money = float(input())

count = 0
while money >= 0.01:
    if money >= 2.00:
        money -= 2.00
    elif money >= 1.00:
        money -= 1.00
    elif money >= 0.5:
        money -= 0.5
    elif money >= 0.2:
        money -= 0.2
    elif money >= 0.1:
        money -= 0.1
    elif money >= 0.05:
        money -= 0.05
    elif money >= 0.02:
        money -= 0.02
    elif money >= 0.01:
        money -= 0.01
    money = round(money, 2)
    count += 1

print(count)