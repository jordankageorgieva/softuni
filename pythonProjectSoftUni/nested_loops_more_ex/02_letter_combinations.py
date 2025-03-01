begin = input()
end = input()
exclude_letter = input()

count = 0
for x1 in range(ord(begin), ord(end) +1):
    if x1 != ord(exclude_letter):
        for x2 in range(ord(begin), ord(end) + 1):
            if x2 != ord(exclude_letter):
                for x3 in range(ord(begin), ord(end) + 1):
                    if x3 != ord(exclude_letter):
                        print(f"{chr(x1)} {chr(x2)} {chr(x3)}")
                        count += 1


print(f"Total combinationas {count}")