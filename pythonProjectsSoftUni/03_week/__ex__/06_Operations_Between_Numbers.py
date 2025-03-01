N1= int(input())
N2 = int(input())
math_operation = input()

if math_operation in ["+", "-", "*"]:
    if math_operation == "+":
        number_type = ''
        if (N1 + N2) % 2 == 0:
            number_type = 'even'
        else:
            number_type = 'odd'

        print(f"{N1} {math_operation} {N2} = {N1 + N2} - {number_type}")
    elif math_operation == "-":
        number_type = ''
        if (N1 - N2) % 2 == 0:
            number_type = 'even'
        else:
            number_type = 'odd'

        print(f"{N1} {math_operation} {N2} = {N1 - N2} - {number_type}")
    elif math_operation == "*":
        number_type = ''
        if (N1 * N2) % 2 == 0:
            number_type = 'even'
        else:
            number_type = 'odd'

        print(f"{N1} {math_operation} {N2} = {N1 * N2} - {number_type}")
elif math_operation in ["/", "%"] and N2 == 0:

    print(f"Cannot divide {N1} by zero")

elif math_operation == "/" and N2 != 0:

    result = float(N1/N2)
    # print(f"{N1} / {N2} = {result:.f02}")
    print(f"{N1} / {N2} = {result:.02f}")
elif math_operation == "%":

    print(f'{N1} % {N2} = {N1 % N2}')
