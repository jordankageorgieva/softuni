age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

sum = 0
money_in = 10
count_toy = 0

for index in range(1,age+1):
    if index % 2 == 0:
        sum += money_in
        sum -= 1
        money_in += 10
    else:
        count_toy += 1

sum_total = sum + count_toy * toy_price

if sum_total >= washing_machine_price:
    print(f"Yes! {sum_total -washing_machine_price:.02f}")
else:
    print(f"No! {washing_machine_price-sum_total:.02f}")