magic_num = int(input())

count = 0
password = ''
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c> d and a*b + c*d == magic_num:
                    count += 1
                    print(f"{a}{b}{c}{d}")
                    if count == 4:
                        password = f"{a}{b}{c}{d}"

if not password:
    print("No!")
else:
    print(f"Password: {password}")
