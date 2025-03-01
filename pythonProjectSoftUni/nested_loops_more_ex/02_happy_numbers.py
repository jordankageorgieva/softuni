num = int(input())

count = 0
for x1 in range (1, 10):
    for x2 in range(1, 10):
        for x3 in range(1, 10):
            for x4 in range(1, 10):
                if x1 + x2 == x3+ x4:
                    if num % (x1 + x2) == 0:
                        print(f"{x1} {x2} {x3} {x4}")
                        count += 1

print(f"happy numbers count {count}")