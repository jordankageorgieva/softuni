book_pages= int(input())
pages_per_one_hour=int(input())
days_number_to_read_the_book = int(input())

total_reading_time=book_pages/pages_per_one_hour
reading_time_per_day = total_reading_time/days_number_to_read_the_book

print(round(reading_time_per_day))