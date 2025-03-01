number_pyramid = int(input())

count = 1
stop_cycle = False
for row in range (0, number_pyramid +1):
    for cow in range(0, number_pyramid + 1):
        print(count, end=" ")
        count += 1
        if count == number_pyramid +1:
            stop_cycle = True
            break
        elif cow >= row:
            break
    if stop_cycle == True:
        break
    print()