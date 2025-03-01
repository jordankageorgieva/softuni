number = int(input())
plate = int(number /2)

index = 2
k = 1
while index <= number - plate:
    for plate2 in range(0, index, 1):
        print(" *", end="")
    index += k
    k += 1
    print()