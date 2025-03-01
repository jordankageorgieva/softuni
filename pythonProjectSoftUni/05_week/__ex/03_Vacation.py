money_trip = int(input())
money_available = int(input())

spend_count = 0
next_iteration = 0
days_total = 0

money_available = money_trip - money_available
action = input()
while action == "spend" or action == "save":
    money = int(input())
    if action == "save":
        spend_count += 1
        money_available += money
        days_total += 1
        print("money available", money_available)
        if money_trip == money_available:
            print(f"You saved the money for {days_total} days.")
            break
    elif action == "spend":
        spend_count -= 1
        money_available -= money
        days_total += 1
        print("money available", money_available)
        print("next iteration", next_iteration)
        if next_iteration == 5:
            print(f"You can't save the money.")
            print(5)
            break
        elif money_available < 0:
            money_available = 0
            next_iteration += 1
        elif next_iteration < 5:
            next_iteration += 1
    action = input()