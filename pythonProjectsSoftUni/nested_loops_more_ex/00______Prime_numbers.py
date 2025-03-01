number = int(input())

for one in range(1 , number + 1):
    if one == 1:
        is_prime = False
    else:
        is_prime = True
        for index in range(2, one):
            if one % index == 0:
                is_prime = False
                break
    print("number ", one, "is priem number ", is_prime)