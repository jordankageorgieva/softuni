last_sector = input()
count_rows_first_sector = int(input())
count_seats_first_row = int(input())

count_total_seats = 0
count_rows_per_sector = count_rows_first_sector
for sector in range(ord('A'), ord(last_sector) +1):
    row = 1
    while row <= count_rows_per_sector:
        if row % 2 != 0:
            for seat in range(ord('a'), ord('b') + 1):
                count_total_seats += 1
                print(f"{chr(sector)} {row} {chr(seat)}")
        else:
            for seat in range(ord('a'), ord('d') + 1):
                count_total_seats += 1
                print(f"{chr(sector)} {row} {chr(seat)}")
        row += 1

    count_rows_per_sector += 1

print(f"count total seats = {count_total_seats}")