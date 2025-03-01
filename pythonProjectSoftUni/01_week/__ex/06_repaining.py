polietilen = int(input())
paint_in_l = int(input())
acid = int(input())
worker_hours = int(input())

sum_polietilen = (polietilen +  2) * 1.50
sum_paint = (paint_in_l  + paint_in_l * 10/100)* 14.50
sum_acid = acid * 5.00
sum_bag = 0.40

materials_total_sum = sum_polietilen + sum_paint + sum_acid + sum_bag

workers_sum = (materials_total_sum * 30/100)  * worker_hours

total_sum = materials_total_sum + workers_sum

print(total_sum)
