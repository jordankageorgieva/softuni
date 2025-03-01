degree = int(input())
day_time= input()

_Outfit = ''
_Shoes = ''
if 10 <= degree <=18:
    if day_time == 'Morning':
        _Outfit = 'Sweatshirt'
        _Shoes = 'Sneakers'
    elif day_time == 'Afternoon':
        _Outfit = 'Shirt'
        _Shoes = 'Moccasins'
    elif day_time == 'Evening':
        _Outfit = 'Shirt'
        _Shoes = 'Moccasins'
elif 18 < degree <= 24:
    if day_time == 'Morning':
        _Outfit = 'Shirt'
        _Shoes = 'Moccasins'
    elif day_time == 'Afternoon':
        _Outfit = 'T-Shirt'
        _Shoes = 'Sandals'
    elif day_time == 'Evening':
        _Outfit = 'Shirt'
        _Shoes = 'Moccasins'
elif degree >= 25:
    if day_time == 'Morning':
        _Outfit = 'T-Shirt'
        _Shoes = 'Sandals'
    elif day_time == 'Afternoon':
        _Outfit = 'Swim Suit'
        _Shoes = 'Barefoot'
    elif day_time == 'Evening':
        _Outfit = 'Shirt'
        _Shoes = 'Moccasins'

if _Outfit and _Shoes:
    print(f"It's {degree} degrees, get your {_Outfit} and {_Shoes}.")