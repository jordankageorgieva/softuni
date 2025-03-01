import math

day = int(input())
kg_food = int(input())
one_deer_food= float(input())
two_deer_food= float(input())
three_deer_food= float(input())

food_total = one_deer_food * day + two_deer_food * day + three_deer_food * day
# print(food_total)
diff = abs(kg_food - food_total)
if food_total < kg_food:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")

