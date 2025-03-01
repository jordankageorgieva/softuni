count = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(count):
    number = int(input())

    if number < 200:
        p1 += 1
    elif 200 <= number < 400:
        p2 += 1
    elif 400 <= number < 600:
        p3 += 1
    elif 600 <= number < 800:
        p4 += 1
    elif number >= 800:
        p5 += 1


p1_in_percentage = p1/ count * 100
p2_in_percentage = p2/ count * 100
p3_in_percentage = p3/ count * 100
p4_in_percentage = p4/ count * 100
p5_in_percentage = p5/ count * 100

print(f"{p1_in_percentage:.02f}%")
print(f"{p2_in_percentage:.02f}%")
print(f"{p3_in_percentage:.02f}%")
print(f"{p4_in_percentage:.02f}%")
print(f"{p5_in_percentage:.02f}%")