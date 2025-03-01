pen_numbers = int(input())
marker_numbers = int(input())
preparat_per_litar = int(input())
discounnt_percentage = int(input())

price_pen = pen_numbers * 5.80
price_markers = marker_numbers * 7.2
price_preparat = preparat_per_litar * 1.2

total_price = price_pen + price_markers + price_preparat

total_price_with_dsicount = total_price -  total_price * (discounnt_percentage/100)

print(total_price_with_dsicount)