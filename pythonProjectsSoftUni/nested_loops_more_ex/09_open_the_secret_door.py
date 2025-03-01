import cmath

num_three = int(input())
num_second = int(input())
num_one = int(input())

count = 0
for three in range(1, num_three +1):
    if three % 2 == 0:
        for two in range(1, num_second + 1):
            if two == 1:
                is_prime = False
            else:
                is_prime = True
                for sub_two in range(2, two):
                    if two % sub_two == 0:
                        is_prime = False
                        break
            # print("two number " , two , "is priem number " , is_prime)
            if is_prime:
                for one in range( 1, num_one +1):
                    if one % 2 == 0:
                        count += 1
                        print(f"{three}{two}{one}")

print(f"count {count}")