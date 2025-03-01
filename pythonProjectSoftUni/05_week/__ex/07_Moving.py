width = int(input())
length = int(input())
height = int(input())

space_cubic = width * height * length
# print("space cubic ",  space_cubic )

sum_cubic = 0
one_dimention_cubic = input()
while one_dimention_cubic != "Done":
    cubic_dimension = int(one_dimention_cubic)
    sum_cubic += cubic_dimension
    # print("sum_cubic ",  sum_cubic )
    if space_cubic <= sum_cubic:
        print(f"No more free space! You need {sum_cubic - space_cubic} Cubic meters more.")
        break
    one_dimention_cubic = input()
else:
    print(f"{space_cubic - sum_cubic} Cubic meters left.")
