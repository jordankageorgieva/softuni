days = int(input())

count = 1
sum_water = 0
sum_degree_per_liter_water = 0

while count <= days:
    water = float(input())
    quantity = float(input())

    if count == 1:
        sum_spirit = water
        quantity = quantity
        sum_degree_per_liter_water = water * quantity

    sum_water += water

    if count > 1:
        sum_degree_per_liter_water += water *quantity
    # print(sum_degree_per_liter_water)
    # sum_water_total += sum_spirit

    count += 1

print(f"Liter: {sum_water:.2f}")
avr_degre = sum_degree_per_liter_water / sum_water
print(f"Degrees: {avr_degre:.2f}")

if avr_degre < 38:
    print("Not good, you should baking!")
elif 38 <= avr_degre <= 42:
    print("Super!")
elif avr_degre > 42:
    print("Dilution with distilled water!")
