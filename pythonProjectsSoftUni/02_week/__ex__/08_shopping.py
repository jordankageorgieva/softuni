peter_budget = float(input())

n_card_video = int(input())
n_process = int(input())
n_ram = int(input())

money_video = n_card_video * 250
money_process = money_video * 35/100 * n_process
money_ram =  money_video * 10/100 * n_ram

money_total = money_video + money_process + money_ram

#discount
if n_card_video > n_process:
    money_total = money_total  - money_total * 15/100

if money_total <= peter_budget:
    print(f"You have {peter_budget - money_total:.02f} leva left!")
else:
    print(f"Not enough money! You need {money_total - peter_budget:.02f} leva more!")