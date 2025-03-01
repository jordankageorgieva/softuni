import sys, select, os

name_player = input()

best_player = ''
best_num_goals= 0
is_hat_trick = False
while True:
    if not name_player or name_player == "END":
        break
    num_goals = int(input())
    if best_num_goals < num_goals:
        best_num_goals = num_goals
        best_player = name_player
        # print(best_num_goals)
        if num_goals >= 3:
            # print(best_num_goals)
            is_hat_trick = True
    try:
        name_player = input()
    except EOFError as e:
            break


print(f"{best_player} is the best player!")
if is_hat_trick:
    print(f"He has scored {best_num_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_num_goals} goals.")