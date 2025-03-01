number = input()

sum_prime_numbers = 0
sum_non_prime_numbers = 0

while number != "stop":
    number_to_int = int(number)
    is_non_prime_number = True
    if number_to_int >= 0:
        # check if number is simple
        for index in range(2, number_to_int):
            if number_to_int % index == 0:
                is_non_prime_number = False
        # print("number ", number_to_int, "is_prime_number ", is_non_prime_number)
        if is_non_prime_number:
            sum_non_prime_numbers += number_to_int
        else:
            sum_prime_numbers += number_to_int
    else:
        print("Number is negative.")
    number = input()

print(f"Sum of all prime numbers is: {sum_non_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_prime_numbers}")