# patterns = ["aaaa", "abbb", "aaab", "aabb", "abab", "abba"]
# def is_magic_car_number(car_number):
#     sum_numbers = 0
#     for index_letter in range(len(car_number)):
#         letter = car_number[index_letter]
#         if letter == "A":
#             sum_numbers += 10
#         elif letter == "B":
#             sum_numbers += 20
#         elif letter == "C":
#             sum_numbers += 30
#         elif letter == "E":
#             sum_numbers += 50
#         elif letter == "H":
#             sum_numbers += 80
#         elif letter == "K":
#             sum_numbers += 110
#         elif letter == "M":
#             sum_numbers += 130
#         elif letter == "P":
#             sum_numbers += 160
#         elif letter == "T":
#             sum_numbers += 200
#         elif letter == "X":
#             sum_numbers += 240
#         elif letter.isdigit():
#             sum_numbers += int(letter)
import time

expected_weight = int(input())
start_time = time.time()

count = 0

def magic_car_test(count):
    for let1 in (
            ord("A"), ord("B"), ord("C"), ord("E"), ord("H"), ord("K"), ord("M"), ord("P"), ord("T"), ord("X")):
        for let2 in (
                ord("A"), ord("B"), ord("C"), ord("E"), ord("H"), ord("K"), ord("M"), ord("P"),
                ord("T"), ord("X")):

            magic_number = f"CA{a_1}{a_2}{a_3}{a_4}{chr(let1)}{chr(let2)}"
            weight = 0
            for i1 in (magic_number):
                if i1 == "A":
                    weight += 10
                elif i1 == "B":
                    weight += 20
                elif i1 == "C":
                    weight += 30
                elif i1 == "E":
                    weight += 50
                elif i1 == "H":
                    weight += 80
                elif i1 == "K":
                    weight += 110
                elif i1 == "M":
                    weight += 130
                elif i1 == "P":
                    weight += 160
                elif i1 == "T":
                    weight += 200
                elif i1 == "X":
                    weight += 240
                else:
                    weight += int(i1)
            if weight == expected_weight:
                print(f"magig_number - CA{a_1}{a_2}{a_3}{a_4}{chr(let1)}{chr(let2)} - weight {weight}")
                count += 1
    return count


for a_1 in range(0, 10):
    for a_2 in range(0, 10):
        for a_3 in range(0, 10):
            for a_4 in range(0, 10):
                # patterns = ["aaaa"]
                if a_1 == a_2 and a_1 == a_3 and a_1 == a_4:
                    count = magic_car_test(count)
                # patterns = ["abbb"]
                elif a_1 != a_2 and a_2 == a_3 and a_2 == a_4:
                    count = magic_car_test(count)
                # # patterns = ["aaab"]
                elif a_1 == a_2 and a_1 == a_3 and a_1 != a_4:
                    count = magic_car_test(count)
                # # patterns = ["aabb"]
                elif a_1 == a_2 and a_3 == a_4 and a_1 != a_3:
                    count = magic_car_test(count)
                # # patterns = ["abab"]
                elif a_1 == a_3 and a_2 == a_4 and a_1 != a_2:
                    count = magic_car_test(count)
                # # patterns = "abba"
                elif a_1 == a_4 and a_2 == a_3 :
                    count = magic_car_test(count)

print(f"count = {count}")
print("--- %s seconds ---" % (time.time() - start_time))