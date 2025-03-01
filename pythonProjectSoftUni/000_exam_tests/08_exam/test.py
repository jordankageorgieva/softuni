# 'A', 'B', 'C', 'E', 'H', 'K', 'M', 'P', 'T', 'X'
# print(ord("A"))
# print(ord("B"))
# print(ord("C"))
# print(ord("E"))
# print(ord("H"))
# print(ord("K"))
# print(ord("M"))
# print(ord("P"))
# print(ord("T"))
# print(ord("X"))

# for let in (ord("A"),ord("B"),ord("C"),ord("E"),ord("H"),ord("K"),ord("M"),ord("P"),ord("T"),ord("X")):
#     print(chr(let))
magic_number = "CA1111AA"
weight = 0
for i1 in (magic_number):
    if i1 == "A":
        weight += 10
    elif i1 == "B":
        weight += 20
    elif i1 == "C":
        weight += 30
    elif i1 == "E":
        weight += 50
    elif i1 == "H":
        weight += 80
    elif i1 == "K":
        weight += 110
    elif i1 == "M":
        weight += 130
    elif i1 == "P":
        weight += 160
    elif i1 == "T":
        weight += 200
    elif i1 == "X":
        weight += 240
    else:
        weight += int(i1)

print(weight)

print(3444456%10)


