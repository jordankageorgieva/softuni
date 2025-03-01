number = int(input())

for index in range(0, number+1):
    if index % 2 == 0:
        print(2 ** index)