fruit = str(input())
week_day = str(input())
quantity = float(input())

price = 0
if week_day in ['Monday', 'Tuesday', 'Wednesday','Thursday','Friday']:
    if fruit == 'banana':
        price = quantity * 2.5
    elif fruit == 'apple':
        price = quantity * 1.2
    elif fruit ==  'orange':
        price = quantity * 0.85
    elif fruit == 'grapefruit':
        price = quantity * 1.45
    elif fruit == 'kiwi':
        price = quantity * 2.70
    elif fruit == 'pineapple':
        price = quantity * 5.50
    elif fruit == 'grapes':
        price = quantity * 3.85
elif week_day in ['Saturday', 'Sunday']:
    if fruit == 'banana':
        price = quantity * 2.70
    elif fruit == 'apple':
        price = quantity * 1.25
    elif fruit ==  'orange':
        price = quantity * 0.9
    elif fruit == 'grapefruit':
        price = quantity * 1.60
    elif fruit == 'kiwi':
        price = quantity * 3.0
    elif fruit == 'pineapple':
        price = quantity * 5.60
    elif fruit == 'grapes':
        price = quantity * 4.20

if price != 0:
    print(f"{price:.02f}")
else:
    print('error')