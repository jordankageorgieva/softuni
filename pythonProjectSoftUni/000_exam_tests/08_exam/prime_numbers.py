n_1 = int(input())
n_2 = int(input())
magic_num = int(input())

combination_count = 0
check = False

for i in range(n_1, n_2 + 1):
    for j in range(n_1, n_2 + 1):
        combination_count += 1
        if i + j == magic_num:
            print(f'Combination N:{combination_count} ({i} + {j} = {magic_num})')
            check = True
            break
    if check:
        break

else:
    print(f' {combination_count} combinations - neither equals {magic_num}')