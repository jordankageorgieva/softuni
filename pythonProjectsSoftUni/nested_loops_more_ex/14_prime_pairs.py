num1 = int(input())
num2 = int(input())
difference1 = int(input())
difference2 = int(input())


def is_prime(number):
    is_prime = False
    if number == 1:
        is_prime = False
    else:
        is_prime = True
        for index in range(2, number):
            if number % index == 0:
                is_prime = False
                break
    # print("number ", number, "is prime number ", is_prime)
    return is_prime


for x1 in range(num1, num1 + difference1 + 1):
    if is_prime(x1) :
        for x2 in range(num2, num2 + difference2 + 1):
            if is_prime(x2):
                print(f"{x1}{x2}")



