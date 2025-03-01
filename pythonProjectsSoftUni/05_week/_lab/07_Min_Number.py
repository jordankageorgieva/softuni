the_min_number = input()
number = 'Go'
while True:
    if number == "Stop":
        print(the_min_number)
        break
    else:
        number = input()
        if number == "Stop":
            continue
        elif int(number) < int(the_min_number):
            the_min_number = number
        continue