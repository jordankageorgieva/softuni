number_unsatisfactory_grade = int(input())

number_problems = 0
sum_problems = 0
is_read_continue = True
get_break = False
last_problems = ""
count_unsatisfied_grade = 0

while is_read_continue:
    task_name = input()
    if task_name == "Enough":
        is_read_continue = False
    else:
        grade = int(input())
        if grade <= 4:
            count_unsatisfied_grade +=1
            if count_unsatisfied_grade == number_unsatisfactory_grade:
                get_break = True
                break
        number_problems += 1
        sum_problems += grade
        last_problems = task_name
        # print("last book ", last_problems)
        # print("sum grade", sum_problems)

if not is_read_continue:
    average_score = sum_problems / number_problems
    print(f"Average score: {average_score:.02f}")
    print(f"Number of problems: {number_problems}")
    print(f"Last problem: {last_problems}")
elif get_break:
    print(f"You need a break, {number_unsatisfactory_grade} poor grades.")

