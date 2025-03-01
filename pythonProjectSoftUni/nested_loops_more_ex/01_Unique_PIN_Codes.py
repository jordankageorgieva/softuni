num1 = int(input())
num2 = int(input())
num3 = int(input())

for x2 in range(1, num2 + 1):
    is_x_prime = True
    for inx in range(2, x2):
        if x2 % inx == 0:
            is_x_prime = False
            print("non prime number" , x2)
            break
    if is_x_prime:
        print("prime number" , x2)

for x1 in range(2, num1 + 1):
    if x1 % 2 == 0:
        for x2 in range(2, num2 +1):
            is_x2_prime = True
            for inx in range(2, x2):
                if x2 % inx == 0:
                    is_x2_prime = False
            if is_x2_prime:
                for x3 in range(1, num3 + 1):
                    if x3 % 2 == 0:
                        print(f"{x1} {x2} {x3}")
            # is_x2_prime = False
            # for inx in range(1, x2):
            #     if x2 % inx == 0:
            #         is_x2_prime = True
            #
            # # print(f"{x1} {x2} {x3}")
            # if  x1 % 2 == 0 and is_x2_prime and x3% 2 == 0:
            #     print(f"{x1} {x2} {x3}")

