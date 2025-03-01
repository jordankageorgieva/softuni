distance = input()
while distance != "End":
    money_min = float(input())

    money_total = 0
    while money_total != money_min:
        money_in = float(input())
        money_total += money_in
        if money_total >= money_min:
            print(f"Going to {distance}!")
            break

    distance = input()