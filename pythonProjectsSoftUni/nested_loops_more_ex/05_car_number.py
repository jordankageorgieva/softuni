begin = int(input())
end = int(input())

for x1 in range(begin, end + 1):
    for x2 in range(begin, end + 1):
        for x3 in range(begin, end + 1):
            for x4 in range(begin, end + 1):
                if x1 % 2 == 0 and x4 % 2 != 0:
                    if x1 > x4:
                        if (x2 + x3) % 2 == 0:
                            print(f"{x1} {x2} {x3} {x4}")
                elif x1 % 2 != 0 and x4 % 2 == 0:
                    if x1 > x4:
                        if (x2 + x3) % 2 == 0:
                            print(f"{x1} {x2} {x3} {x4}")