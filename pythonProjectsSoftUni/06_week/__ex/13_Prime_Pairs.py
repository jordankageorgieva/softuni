num_magic = int(input())

count_four_sequence = 0
password_correct = 0
for num in range (1111, 9999 +1):
    num_as_str = str(num)
    a = int(num_as_str[0])
    b = int(num_as_str[1])
    c = int(num_as_str[2])
    d = int(num_as_str[3])

    if a < b and c > d and (a*b + c*d) == num_magic:
        print(num, end=" ")
        # print("num : ", num)
        count_four_sequence += 1
        if count_four_sequence == 4:
            # print("password_correct : ", num)
            password_correct = num


if count_four_sequence != 0:
    print(f"Password: {password_correct}")
else:
    print("No!")