hour = int(input())
minutes = int(input())

mins_with_add_15_min = minutes + 15
if mins_with_add_15_min < 60:
    print(f"{hour}:{mins_with_add_15_min:02d}")
else:
    new_mins = mins_with_add_15_min % 60
    new_hour = hour + 1

    if new_hour == 24:
        new_hour = 0

    print(f"{new_hour}:{new_mins:02d}")

