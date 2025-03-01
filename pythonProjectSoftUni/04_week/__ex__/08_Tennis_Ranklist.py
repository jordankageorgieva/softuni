import math

turnaments_count = int(input())
points_turnaments = int(input())

sum_points = points_turnaments
winner_count = 0

for _ in range (turnaments_count):
    stage_turnament = input()
    if stage_turnament == "W":
        sum_points += 2000
        winner_count += 1
    elif stage_turnament == "F":
        sum_points += 1200
    elif stage_turnament == "SF":
        sum_points += 720

average_points = math.floor((sum_points - points_turnaments) /turnaments_count)

percentage = winner_count /turnaments_count * 100

print(f"Final points: {sum_points}")
print(f"Average points: {average_points:.00f}")
print(f"{percentage:.02f}%")