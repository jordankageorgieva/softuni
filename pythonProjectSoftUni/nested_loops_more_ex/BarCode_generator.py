n_1 = int(input())
n_2 = int(input())

n_1_to_str = str(n_1)
i_1 = n_1_to_str[0]
i_2 = n_1_to_str[1]
i_3 = n_1_to_str[2]
i_4 = n_1_to_str[3]

n_2_to_str = str(n_2)
j_1 = n_2_to_str[0]
j_2 = n_2_to_str[1]
j_3 = n_2_to_str[2]
j_4 = n_2_to_str[3]

# print("int(i_1)", int(i_1) , "int(j_1)", int(j_1))
for x_1 in range(int(i_1) , int(j_1) + 1):
    for x_2 in range(int(i_2), int(j_2) + 1):
        for x_3 in range(int(i_3), int(j_3) + 1):
            for x_4 in range(int(i_4), int(j_4) + 1):
                if x_1 % 2 != 0 and x_2 % 2 != 0 and x_3 % 2 != 0 and x_4 % 2 != 0:
                    print(f"{x_1}{x_2}{x_3}{x_4}", end = " ")