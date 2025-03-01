the_biggest_number = input()
number = 'Go'
while True:
    if number == "Stop":
        print(the_biggest_number)
        break
    else:
        number = input()
        if number == "Stop":
            continue
        elif int(number) > int(the_biggest_number):
            the_biggest_number = number
        continue