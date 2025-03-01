# bee_groups = [int(e) for e in input().split()]
bee_plus = [32, 42, 7, 28, 3]
# bee_plus = [21, 14, 14 ,7]
# bee_eaters = [int(e) for e in input().split()]
bee_minus = [1 ,5, 6]
bee_minus_reverse = bee_minus.reverse()
# bee_minus = [1, 2, 2, 3]

bee_plus_length = len(bee_plus)
bee_minus_length = len(bee_minus)

len = 0
if bee_plus_length > bee_minus_length:
    len = bee_plus_length
else:
    len = bee_minus_length

new_bee_minus_reverse = bee_minus_reverse
index = 0
while index <= len:
    if (bee_plus[index] == bee_minus_reverse[index] * 7 ):
        print("Equals Battle")
        index += 1
    elif bee_plus[index] < bee_minus_reverse[index] * 7:
        hunters = bee_plus[index] % 7
        print("new hunters : ", bee_minus_reverse[index] - hunters)
        new_bee_minus_reverse[index] = bee_minus_reverse[index] - hunters
        new_bee_plus = bee_plus.remove()


# bee_plus_plus = 0
# bee_minus_minus = 0
# flag_changed = False
# for index in range(0, len(bee_plus)):
#     print(f"row {index} value {bee_plus[index]}")
#     bee_to_beat = bee_plus[index] + bee_plus_plus
#     battle_bee_killed = bee_to_beat// 7
#     battle_survivers = bee_to_beat % 7
#     print(f" oceleli pcheli {battle_survivers}")
#     print(bee_minus[len(bee_minus) - index -1])
#     battle_real_survivers = battle_survivers
#     # unwinners bee
#     if bee_minus[len(bee_minus) - index -1] > battle_survivers or flag_changed != False:
#         bee_minus_minus = bee_minus[len(bee_minus) - index -1] - battle_survivers
#         bee_minus[len(bee_minus) - index - 1] = bee_minus[len(bee_minus) - index -1] - battle_survivers
#         flag_changed = True
#     # winners bee
#     else:
#         bee_winne = bee_to_beat - bee_minus[len(bee_minus) - index -1] * 7
#         bee_plus[len(bee_plus) - 1] = bee_plus[len(bee_plus) - 1] - bee_winne
#
#
#     # if battle_survivers > 0:
#     #     battle_real_survivers = battle_survivers
#         # if len(bee_eaters) - index -1 >= 0:
#         #  battle_real_survivers = bee_eaters[len(bee_eaters) - index -1] - battle_survivers + battle_real_survivers
#         #  print(f"iteration {index} - oceleli pcheli {battle_real_survivers}")
#         # elif battle_real_survivers > 0:
#         #     battle_real_survivers = - battle_survivers + battle_real_survivers
#         #     print(f"iteration no data in second list {index} - oceleli pcheli {battle_real_survivers}")
#         # else:
#         #     break
#     print(f"battle_real_survivers {battle_real_survivers}")
#
# print("The final battle is over!")
# print(f"final battle_real_survivers {bee_plus_plus}")
# if bee_plus_plus == 0:
#     print(f"But no one made it out alive!")
# elif bee_plus_plus > 0:
#     print(f"Bee-eater groups left: {bee_plus_plus}")

# for index_eat in range(len(bee_eaters), 0, -1):
#          print(bee_eaters[index_eat])