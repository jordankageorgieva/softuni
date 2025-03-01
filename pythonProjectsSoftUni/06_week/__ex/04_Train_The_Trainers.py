num_prersons = int(input())

sum_avr_grade = 0
presentation = input()
presentation_count = 0
while presentation != "Finish":

    sum_grade = 0
    for index in range(1, num_prersons +1):
        grade = float(input())
        sum_grade += grade

    avr_grade = sum_grade / num_prersons
    print(f"{presentation} - {avr_grade:.02f}.")
    sum_avr_grade += avr_grade
    presentation_count += 1
    presentation = input()

total_avr_grade = sum_avr_grade / presentation_count
print(f"Student's final assessment is {total_avr_grade:.02f}.")