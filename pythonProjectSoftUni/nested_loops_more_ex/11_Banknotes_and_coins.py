count_one_currency = int(input())
count_two_currency = int(input())
count_five_currency = int(input())
sum = int(input())

for x1 in range(0, count_one_currency +1):
    for x2 in range(0, count_two_currency +1):
        for x3 in range(0, count_five_currency +1):
            if x1*1 + x2*2 + x3*5 == sum:
                print(f"{x1} * 1 lv. + {x2} * 2 lv. + {x3} * 5 lv. = {sum} lv.")