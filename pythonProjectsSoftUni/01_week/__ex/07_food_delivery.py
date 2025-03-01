chicken_menu_number = int(input())
fish_menu_number = int(input())
vegan_menu_number = int(input())

price_chicken = chicken_menu_number * 10.35
price_fish = fish_menu_number * 12.40
price_vegan = vegan_menu_number * 8.15

total_price = price_chicken + price_fish + price_vegan

desert_price = total_price * 20/100
delivery_price = 2.50

total_order_price = total_price + desert_price + delivery_price

print(round(total_order_price, 2))