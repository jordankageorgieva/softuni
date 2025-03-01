count_days = int(input())
count_hours = int(input())

money_total = 0
for day in range(1, count_days + 1):
    money = 0
    for hour in range(1, count_hours + 1):
         if day % 2 != 0 and hour % 2 == 0:
             money += 1.25
         elif day % 2 != 0 and hour % 2 != 0:
             money += 1
         elif day % 2 == 0 and hour % 2 != 0:
             money += 2.5
         elif day % 2 == 0 and hour % 2 == 0:
             money += 1

    money_total += money
    print(f"Day: {day} - {money:.02f} leva")

print(f"Total: {money_total:.02f} leva")