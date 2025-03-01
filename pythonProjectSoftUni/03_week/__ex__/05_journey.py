budget = float(input())
season = input()

entity_camp_or_hotel = ''
money = 0.0
if budget <= 100:
    distance = 'Bulgaria'
    if season == 'summer':
        entity_camp_or_hotel = 'Camp'
        money = budget * 0.3
    elif season == 'winter':
        entity_camp_or_hotel = 'Hotel'
        money = budget * 0.7
elif budget <= 1000:
    distance = 'Balkans'
    if season == 'summer':
        entity_camp_or_hotel = 'Camp'
        money = budget * 0.4
    elif season == 'winter':
        entity_camp_or_hotel = 'Hotel'
        money = budget * 0.8
elif budget > 1000:
    distance = 'Europe'
    entity_camp_or_hotel = 'Hotel'
    money = budget * 0.9


print(f'Somewhere in {distance}')
print(f'{entity_camp_or_hotel} - {money:.02f}')