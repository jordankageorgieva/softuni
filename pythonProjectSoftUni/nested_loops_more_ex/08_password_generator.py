a = int(input())
b = int(input())
max_pass = int(input())

internal_break = False
b1 = 64
a1 = 35
count = 0
for x in range(1, a + 1):
    # for y in range(1, b + 1):
        y = 1
        while y <= b and b1 < 97 and a1 < 56:
            # for a1 in range(35, 55 + 1):
            # for b1 in range(64, 96 + 1):
            print(f"{chr(a1)}{chr(b1)}{x}{y}{chr(b1)}{chr(a1)}")
            count += 1
            if count >= max_pass:
                internal_break = True
                break
            y += 1
            if a1 < 56:
                a1 += 1
            else:
                a1 = 35
            if b1 < 97:
                b1 += 1
            else:
                b1 = 97
        if internal_break:
            break
print(f"count {count}")