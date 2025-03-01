number = int(input())

count = 0
for x1 in range(1, number + 1):
    for x2 in range(1,number + 1):
       if x2 < count +1  or x2 > number - count:
           print(f".", end=" ")
       else:
           print(f"*", end=" ")
    if x1 <= number/2:
        count += 1
    else:
        count -= 1
    print()
