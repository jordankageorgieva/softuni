width = int(input())
length = int(input())
height = int(input())
percentage = float(input())

volume = width * length * height
volume_in_l = volume * 0.001
occupied_space = percentage/100
necessary_water_l = volume_in_l * (1-occupied_space)

print(necessary_water_l)