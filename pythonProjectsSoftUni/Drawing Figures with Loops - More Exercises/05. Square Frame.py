num = int(input())

# upper part
print("+", end = " ")
for x1 in range(0, num - 2):
    print("-", end=" ")
print("+", end = " ")
print()
# middle part
for x2 in range (0, num- 2):
    print("|", end = " ")
    for x3 in range( 0, num - 2):
        print("-", end=" ")
    print("|")
# bottom part
print("+", end = " ")
for x1 in range(0, num - 2):
    print("-", end=" ")
print("+", end = " ")
print()