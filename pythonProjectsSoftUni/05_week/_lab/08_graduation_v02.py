name_of_student = input()
grades_counter = 0
years_counter = 0
failed_counter = 0

while years_counter < 12:
    annual_grade = float(input())
    years_counter += 1

    if annual_grade < 4:
        failed_counter += 1
        if failed_counter > 1:
            print(f"{name_of_student} has been excluded at {years_counter} grade")
            break
        years_counter -= 1
        continue
    grades_counter += annual_grade
else:
    average_grade = grades_counter / 12
    print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")
