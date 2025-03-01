command = input()
best_player = ''
best_num_goals= 0
is_hat_trick = False
while True:
    if command == "End":
        break
    elif not command:
        break
    goals = int(input())
    if best_num_goals < goals:
        best_num_goals = goals
        best_player = command
        # print(best_num_goals)
        if goals >= 3:
            # print(best_num_goals)
            is_hat_trick = True
    command = input()


print(f"{best_player} is the best player!")
if is_hat_trick:
    print(f"He has scored {best_num_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_num_goals} goals.")