number = int(input())

 # head traingle
for plate in range(0, number, 1):
    index = plate + plate
    j = 0
    while j < index/2:
        print(".",end=" ")
        j += 1
    while index <= number-1:
        print("*", end=" ")
        index += 1
    if j <= index/2:
        print()
       # else:
    #     print("888888")
# tail traingle
