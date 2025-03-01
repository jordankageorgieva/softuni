yard_greening = int(input())

total_price_greening = yard_greening * 7.61

final_price_greening = total_price_greening * (1 - 0.18)

discount = round(total_price_greening -final_price_greening, 2)

print(final_price_greening)
print(discount)