num = int(input())

num2 = num -1

elements_on_the_row = num + num2
# upper row
print(elements_on_the_row)
for _ in range(1, elements_on_the_row -num +1 ):
    print(" ", end="")
print("*", end="")
for _ in range(1, elements_on_the_row -num +1 ):
    print(" ", end="")

# middle row
print()
if num % 2 == 0:
    start_el = "*"
else:
    start_el = " "
for _ in range(1, elements_on_the_row):
    for _ in range(1, elements_on_the_row ):
        if start_el == " ":
            print(start_el, end="")
            start_el ="*"
        if start_el == "*":
            print(start_el, end="")
            start_el = " "
    print()