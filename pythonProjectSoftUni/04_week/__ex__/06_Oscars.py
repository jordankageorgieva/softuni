actor_name = input()
points = float(input())
count_assesment = int(input())

# print(f"points : {points:.01f}")
for _ in range(1, count_assesment + 1):
    assesment_name =  input()
    points_assesment_name = float(input())
    points += (len(assesment_name) * points_assesment_name) / 2
    # print(f"add points {(len(assesment_name) * points_assesment_name) / 2}")
    # print(f"points : {points:.01f}")
    if points >= 1250.5:
        break

if points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.01f}!")
else:
    print(f"Sorry, {actor_name} you need {1250.5 - points:.01f} more!")