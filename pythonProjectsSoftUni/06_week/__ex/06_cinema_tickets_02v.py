command = input()

count_standard = 0
count_kids = 0
count_student = 0
while command != "Finish":
    cinema = command
    seat_available = int(input())

    ticket_type = input()
    seats_taken = 0
    while ticket_type != "End":
        if ticket_type == "standard":
            count_standard += 1
        elif ticket_type == "kid":
            count_kids += 1
        elif ticket_type == "student":
            count_student += 1
        seats_taken += 1

        if seats_taken >= seat_available:
            break

        ticket_type = input()

    # total_tickets += count_seat
    percentage_movie_full = seats_taken / seat_available * 100
    print(f"{cinema} - {percentage_movie_full:.02f}% full.")
    command = input()

total_tickets = count_kids + count_student + count_standard
print(f"Total tickets: {total_tickets}")
student = count_student / total_tickets * 100
print(f"{student:.02f}% student tickets.")
# print("count_standards ", count_standards)
standard = count_standard / total_tickets * 100
print(f"{standard:.02f}% standard tickets.")
# print("count_kids ", count_kids)
kids = count_kids / total_tickets * 100
print(f"{kids:.02f}% kids tickets.")