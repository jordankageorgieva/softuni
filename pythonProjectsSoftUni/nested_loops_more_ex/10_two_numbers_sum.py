num1 = int(input())
num2 = int(input())
num_magic = int(input())

count = 0
stop_cycle_at_first_combination = False
for x1 in range(num1, num2 + 1):
    for x2 in range(num1, num2 + 1):
        count += 1
        if x1 + x2 == num_magic:
            print(f"Combination N:{count} ({x1} + {x2} = {num_magic})")
            stop_cycle_at_first_combination = True
            break
    if stop_cycle_at_first_combination:
        break

if not stop_cycle_at_first_combination:
    print(f"{count} combinations - neither equals {num_magic}")