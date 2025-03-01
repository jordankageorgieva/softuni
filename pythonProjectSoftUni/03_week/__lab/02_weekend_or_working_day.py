day_str = str(input())

if day_str == "Monday" or day_str == "Tuesday" \
        or day_str == "Wednesday" or day_str == "Thursday" \
        or day_str == "Friday":
               print("Working day")
elif day_str in ["Saturday","Sunday"]:
    print("Weekend")
else:
    print("Error")

# if day_str in ["Monday", "Tuesday", "Wednesday", "Thursday","Friday"]:
#                print("Working day")
# elif day_str in ["Saturday","Sunday"]:
#     print("Weekend")
# else:
#     print("Error")

# "Thursday","Friday","Saturday","Sunday"