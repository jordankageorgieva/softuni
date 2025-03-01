import math

figure_type = str(input())

if figure_type.__eq__("square"):
    side = float(input())
    area = side * side
    print(f"{area:.3f}")
elif figure_type.__eq__("rectangle"):
    width = float(input())
    height = float(input())
    area = width * height
    print(f"{area:.3f}")
elif figure_type.__eq__("circle"):
    radius = float(input())
    # print(round(math.pi,3))
    # print(math.pi)
    area = math.pi * radius * radius
    print(f"{area:.3f}")
elif figure_type.__eq__("triangle"):
    side = float(input())
    height = float(input())
    area = side * height / 2
    print(f"{area:.3f}")