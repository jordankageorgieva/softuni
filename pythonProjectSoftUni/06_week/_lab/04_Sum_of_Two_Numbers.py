number1 = int(input())
number2 = int(input())
magic_number = int(input())

count = 0
stop_cicle = False
for x1 in range(number1, number2+1):
    for x2 in range(number1, number2+1):
        sum = x1 + x2
        # print("sum ", sum, "x1 =", x1, "x2 =", x2)
        if sum == magic_number:
            print(f"Combination N:{count+1} ({x1} + {x2} = {sum})")
            stop_cicle = True
            break
        count += 1
    if stop_cicle == True:
        break

if stop_cicle == False:
    print(f"{count} combinations - neither equals {magic_number}")
