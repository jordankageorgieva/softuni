num = int(input())

x1 = 1
while x1 <= num:
    for x2 in range(1, x1 + 1):
        print("$" , end = " ")
    print()
    x1 += 1