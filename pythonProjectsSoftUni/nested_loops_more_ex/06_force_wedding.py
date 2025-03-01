man = int(input())
women = int(input())
tables = int(input())

count = 0
stop = False
for m in range(1, man + 1):
    for w in range(1, women + 1):
        count += 1
        print(f"({m} <-> {w})", end=" ")
        if count >= tables:
            stop = True
            break
    if stop:
        break
