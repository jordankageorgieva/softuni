days_vacation = int(input())
room_vacation = input()
assessment_vacation = input()

nights = days_vacation - 1
money = 0.0
if nights < 10:
    if room_vacation == 'room for one person':

        money = (nights * 18.00)

        if assessment_vacation == 'positive':
            money = money + money * 0.25
        elif assessment_vacation == 'negative':
            money = money - money * 0.10

    elif room_vacation == 'apartment':

        money = (nights * 25.00)

        money = money * (1 - 0.3)
        if assessment_vacation == 'positive':
            money = money + money * 0.25
        elif assessment_vacation == 'negative':
            money = money - money * 0.10

    elif room_vacation == 'president apartment':

        money = (nights * 35.00)
        money = money * (1 - 0.1)
        if assessment_vacation == 'positive':
            money = money + money * 0.25
        elif assessment_vacation == 'negative':
            money = money - money * 0.10


elif 10 <= nights <= 15:
    if room_vacation == 'room for one person':

        money = (nights * 18.00)

        if assessment_vacation == 'positive':
            money = money + money * 0.25
        elif assessment_vacation == 'negative':
            money = money - money * 0.10

    elif room_vacation == 'apartment':

        money = (nights * 25.00)

        money = money * (1 - 0.35)
        if assessment_vacation == 'positive':
            money = money + money * 0.25
        elif assessment_vacation == 'negative':
            money = money - money * 0.10

    elif room_vacation == 'president apartment':

        money = (nights * 35.00)
        money = money * (1 - 0.15)
        if assessment_vacation == 'positive':
            money = money + money * 0.25
        elif assessment_vacation == 'negative':
            money = money - money * 0.10
elif nights > 15:
    if room_vacation == 'room for one person':

        money = (nights * 18.00)

        if assessment_vacation == 'positive':
            money = money + money * 0.25
        elif assessment_vacation == 'negative':
            money = money - money * 0.10

    elif room_vacation == 'apartment':

        money = (nights * 25.00)

        money = money * (1 - 0.50)
        if assessment_vacation == 'positive':
            money = money + money * 0.25
        elif assessment_vacation == 'negative':
            money = money - money * 0.10

    elif room_vacation == 'president apartment':

        money = (nights * 35.00)
        money = money * (1 - 0.20)
        if assessment_vacation == 'positive':
            money = money + money * 0.25
        elif assessment_vacation == 'negative':
            money = money - money * 0.10


print(f"{money:.02f}")