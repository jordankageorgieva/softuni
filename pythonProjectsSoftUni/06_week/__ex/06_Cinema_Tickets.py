film = input()
free_seat = int(input())

total_tickets = 0
go_out_from_all_cycles = False
count_students = 0
count_standards = 0
count_kids = 0
count_total = 0
while film != "Finish":
    type_seat = input()
    count_seat = 0
    count_total += free_seat
    while type_seat != "End":
        if type_seat in ("standard", "kid", "student"):
            if type_seat == "standard":
                count_standards += 1
            elif type_seat == "kid":
                count_kids += 1
            elif type_seat == "student":
                count_students += 1
            count_seat += 1
        elif type_seat == "Finish":
            go_out_from_all_cycles = True
            break
        type_seat = input()

    total_tickets += count_seat
    percentage_movie_full = count_seat / free_seat * 100
    print(f"{film} - {percentage_movie_full:.02f}% full.")
    if go_out_from_all_cycles:
        break
    film = input()
    free_seat = int(input())

print(f"Total tickets: {total_tickets}")
# print("count_students ", count_students)
student = count_students / total_tickets * 100
print(f"{student:.02f}% student tickets.")
# print("count_standards ", count_standards)
standard = count_standards / total_tickets * 100
print(f"{standard:.02f}% standard tickets.")
# print("count_kids ", count_kids)
kids = count_kids / total_tickets * 100
print(f"{kids:.02f}% kids tickets.")