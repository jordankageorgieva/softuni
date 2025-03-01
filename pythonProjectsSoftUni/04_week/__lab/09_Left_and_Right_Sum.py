count = int(input())

sum_left = 0
for index in range(1, count + 1):
    number = int(input())
    sum_left += number

sum_right = 0
for index in range(1, count + 1):
    number = int(input())
    sum_right += number

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
elif sum_left < sum_right:
    print(f"No, diff = {sum_right - sum_left}")
elif sum_left > sum_right:
    print(f"No, diff = {sum_left - sum_right}")