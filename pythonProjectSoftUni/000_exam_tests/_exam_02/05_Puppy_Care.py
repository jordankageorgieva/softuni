kg_food = int(input())

sum = 0
while True:
    g_per_eat = input()
    if g_per_eat == "Adopted":
        break
    else:
        sum += int(g_per_eat)


if sum <= kg_food * 1000:
    diff = kg_food * 1000 - sum
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    diff = sum - kg_food * 1000
    print(f"Food is not enough. You need {diff} grams more.")


