count_fl = int(input())
count_rooms = int(input())

for fl in range(count_fl, 0, -1):
    if  fl == count_fl:
        # large apartment
        for room in range(0, count_rooms):
            print(f"L{fl}{room}", end=" ")
    elif  fl % 2 != 0:
          # apartment
        for room in range(0, count_rooms):
            print(f"A{fl}{room}", end=" ")
    elif fl % 2 == 0:
       for room in range(0, count_rooms):
           # office
           print(f"O{fl}{room}", end=" ")
    print()