num1 = int(input())
num2 = int(input())

for num in range(num1, num2+1):
    num_as_str = str(num)
    sum_odd = 0
    sum_even = 0
    for index in range(len(num_as_str)):
        # print("index", index)
        if index % 2 == 0:
            # print("num_as_str[{index}]", num_as_str, index)
            # int_num = int(num_as_str)
            # print(num_as_str[0])
            sum_even += int(num_as_str[index])
        else:
            sum_odd += int(num_as_str[index])
    # print("num = ", num, "sum_even = ", sum_even, "sum_odd = ", sum_odd)
    if sum_even == sum_odd:
        print(num, end=" ")
