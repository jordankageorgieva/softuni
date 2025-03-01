film_type = input()
number_rows = int(input())
number_columns_room = int(input())

number_seats = 0
if number_rows != 0 and number_columns_room != 0:
    number_seats = number_rows * number_columns_room

money_in = 0.0

if film_type == 'Premiere':
    money_in = number_seats * 12.00
elif film_type == 'Normal':
    money_in = number_seats * 7.50
elif film_type == 'Discount':
    money_in = number_seats * 5.00

if money_in != 0:
    print(f"{money_in:.02f} leva")