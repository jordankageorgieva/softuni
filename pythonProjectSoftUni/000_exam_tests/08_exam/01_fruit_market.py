price_strawberry = float(input())
q_bananas = float(input())
q_oranges = float(input())
q_raspberries = float(input())
q_strawberry = float(input())

price_raspberries = price_strawberry * 0.5
price_oranges = price_raspberries * (1 - 0.4)
price_bananas = price_raspberries * (1 - 0.8)

money = q_strawberry * price_strawberry + q_raspberries * price_raspberries \
        + q_oranges * price_oranges + q_bananas * price_bananas

print(f"{money:.02f}")