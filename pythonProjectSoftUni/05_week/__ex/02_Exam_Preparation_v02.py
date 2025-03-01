number_unsatisfactory_grade = int(input())

count_unsatisfied_grade = 0
number_problems = 0
sum_problems = 0

task_name = input()
while task_name != "Enough":
    grade = int(input())
    if grade <= 4:
        count_unsatisfied_grade += 1
        if count_unsatisfied_grade == number_unsatisfactory_grade:
            print(f"You need a break, {number_unsatisfactory_grade} poor grades.")
            break
    number_problems += 1
    sum_problems += grade
    last_problems = task_name
    # print("last book ", last_problems)
    # print("sum grade", sum_problems)
    task_name = input()
else:
    # print("number_problems ", number_problems)
    # print("sum grade", sum_problems)
    average_score = sum_problems / number_problems
    print(f"Average score: {average_score:.02f}")
    print(f"Number of problems: {number_problems}")
    print(f"Last problem: {last_problems}")
