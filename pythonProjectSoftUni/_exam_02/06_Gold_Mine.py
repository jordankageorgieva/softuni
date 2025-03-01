locations = int(input())

for _ in range(locations):
    avg_gold = int(input())
    days_mine = int(input())
    sum_gold = 0
    for _ in range(days_mine):
        cur_gold = int(input())
        sum_gold += cur_gold
    avr_gold_calc = sum_gold / days_mine
    if avr_gold_calc >= avg_gold:
        print(f"Good job! Average gold per day: {avr_gold_calc:.02f}.")
    else:
        diff = avg_gold - avr_gold_calc
        print(f"You need {diff:.02f} gold.")
