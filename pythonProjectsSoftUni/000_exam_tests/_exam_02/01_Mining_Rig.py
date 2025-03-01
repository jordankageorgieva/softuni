import math

pr_card = int(input())
pr_prehodnik = int(input())
pr_cur_by_card = float(input())
money_cadr = float(input())

pr_cards_total = pr_card * 13

pr_prehodnik_total = pr_prehodnik * 13

money_total = pr_prehodnik_total + pr_cards_total + 1000

money_per_day = money_cadr - pr_cur_by_card

money_per_day_total = money_per_day * 13
days_back = math.ceil(money_total /money_per_day_total)

print(money_total)
print(days_back)
