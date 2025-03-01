name_player = input()

best_player = ''
best_num_goals= 0
is_hat_trick = False
while name_player != "END" and name_player:
    # if name_player == "":
    #     break
    num_goals = int(input())
    if best_num_goals < num_goals:
        best_num_goals = num_goals
        best_player = name_player
        # print(best_num_goals)
        if num_goals >= 3:
            # print(best_num_goals)
            is_hat_trick = True
    name_player = input()
else:
    print(f"{best_player} is the best player!")
    if is_hat_trick:
        print(f"He has scored {best_num_goals} goals and made a hat-trick !!!")
    else:
        print(f"He has scored {best_num_goals} goals.")