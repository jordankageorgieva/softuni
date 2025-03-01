age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

saved_money = 0
toy_counter = 0
money_gift = 10

for birthday in range(1, age +1):
    if birthday % 2 == 0:
        saved_money += money_gift
        saved_money -= 1
        money_gift += 10
    else:
        toy_counter += 1

total_toy_money = toy_counter * toy_price
saved_money += total_toy_money

difference = saved_money - washing_machine_price

if difference >= 0:
    print(f"Yes! {difference:.02f}")
else:
    print(f"No! {abs(difference):.02f}")