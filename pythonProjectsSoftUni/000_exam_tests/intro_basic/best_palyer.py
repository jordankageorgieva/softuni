
best_player = ''
best_num_goals= 0
is_hat_trick = False
while True:
    try:
        name_player = input()
    except EOFError as e:
        break
    if name_player == "END" or not name_player:
        break
    goals = int(input())
    if best_num_goals < goals:
        best_num_goals = goals
        best_player = name_player
        # print(best_num_goals)
        if goals >= 3:
            # print(best_num_goals)
            is_hat_trick = True


print(f"{best_player} is the best player!")
if is_hat_trick:
    print(f"He has scored {best_num_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_num_goals} goals.")