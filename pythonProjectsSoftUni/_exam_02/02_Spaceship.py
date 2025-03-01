import math

width_space_ship = float(input())
length_space_ship = float(input())
height_space_ship = float(input())
height_space_man_avrg = float(input())

volume_space_ship = width_space_ship * length_space_ship * height_space_ship

volume_one_room = (height_space_man_avrg + 0.4) * 2 * 2
# print(volume_one_room)

num_space_men = math.floor(volume_space_ship / volume_one_room)

if 3 <= num_space_men <= 10:
    print(f"The spacecraft holds {num_space_men} astronauts.")
elif num_space_men < 3:
    print("The spacecraft is too small.")
elif num_space_men > 10:
    print("The spacecraft is too big.")