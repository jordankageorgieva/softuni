walk = input()

sum_walk = 0
while walk != "Going home":
    sum_walk += int(walk)
    if sum_walk >= 10_000:
        print("Goal reached! Good job!")
        print(f"{sum_walk -10_000} steps over the goal!")
        break
    walk = input()
else:
    walk = int(input())
    sum_walk += walk
    if sum_walk <= 10_000:
        print(f"{10_000 - sum_walk} more steps to reach goal.")
    else:
        print("Goal reached! Good job!")
        print(f"{sum_walk - 10_000} steps over the goal!")