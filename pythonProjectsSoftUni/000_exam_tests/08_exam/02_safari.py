money_available = float(input())
l_gass = float(input())
day = input()

money_total = l_gass * 2.10 + 100.00

if "Saturday".__eq__(day):
    money_total = money_total * (1-0.1)
elif "Sunday".__eq__(day):
    money_total = money_total * (1-0.2)

if money_total <= money_available:
    print(f"Safari time! Money left: {money_available-money_total:.02f} lv. ")
elif money_total > money_available:
    print(f"Not enough money! Money needed: {money_total - money_available:.02f} lv.")