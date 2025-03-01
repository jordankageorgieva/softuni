total_money = 0
while True:
    money = input()
    if money == "NoMoreMoney":
        break
    else:
        if float(money) > 0:
            total_money += float(money)
            print(f"Increase: {float(money):.02f}")
        else:
            print("Invalid operation!")
            break

print(f"Total: {total_money:.02f}")