num1 = int(input())
num2 = int(input())
num3 = int(input())

for n1 in range(1, num1 +1):
    for n2 in range(2, num2 + 1):
        for n3 in range(1, num3 + 1):
            n2_simple = True
            for n in range (2, n2):
                if n2 % n == 0:
                    n2_simple = False
                    break
            if n1 % 2 == 0 and n3 % 2 == 0 and n2_simple:
                print(f"{n1} {n2} {n3}")