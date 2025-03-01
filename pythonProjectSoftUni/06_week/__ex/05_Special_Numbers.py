input_number = int(input())

for num in range(1_111, 9_999+1):

    is_special_number = True
    # number = 1113
    number_as_str = str(num)
    # print(number_as_str)
    for digit in (number_as_str):
        # print("digit ", digit)
        digit_int = int(digit)
        if digit_int == 0:
            is_special_number = False
            break
        if input_number % digit_int != 0:
            # number is special
            is_special_number = False
            break
    # print(is_special_number)

    if is_special_number:
        print(f"{num}", end=" ")
