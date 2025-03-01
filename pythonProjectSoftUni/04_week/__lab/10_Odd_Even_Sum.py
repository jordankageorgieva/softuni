count = int(input())

sum_odd = 0
sum_even = 0
for index in range(1, count + 1):
    number = int(input())
    if index % 2 == 0:
        sum_odd += number
    else:
        sum_even += number

if sum_odd == sum_even:
    print(f"Yes")
    print(f"Sum = {sum_odd}")
elif sum_odd < sum_even:
    print(f"No")
    print(f"Diff = {sum_even - sum_odd}")
elif sum_odd > sum_even:
    print(f"No")
    print(f"Diff = {sum_odd -sum_even}")