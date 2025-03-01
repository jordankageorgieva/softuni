book_to_search = input()

is_book_found = False

count = 0
while is_book_found == False:
    book = input()
    count += 1
    if book == book_to_search:
        print(f"You checked {count-1} books and found it.")
        is_book_found = True
    elif book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count-1} books.")
        is_book_found = True
