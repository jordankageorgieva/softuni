money_need = float(input())
money_available = float(input())

counter_days =0
counter_spending_days = 0

while money_available < money_need and counter_spending_days < 5:
    command = input()
    money = float(input())
    counter_days += 1
    if command == "save":
        money_available += money
        counter_spending_days = 0
    elif command == "spend":
        money_available -= money
        counter_spending_days += 1
        if money_available < 0:
            money_available = 0

if counter_spending_days == 5:
    print("You can't save the money.")
    print(f"{counter_days}")

if money_available >= money_need:
    print(f"You saved the money for {counter_days} days.")