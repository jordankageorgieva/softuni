width = int(input())
height = int(input())

numbers_cake = width * height

while True:
    reduce_cake = input()
    if reduce_cake == "STOP":
       print(f"{numbers_cake} pieces are left.")
       break
    else:
        cakes_to_remove = int(reduce_cake)
        numbers_cake -= cakes_to_remove

        if numbers_cake <= 0:
            print(f"No more cake left! You need {abs(numbers_cake)} pieces more.")
            break