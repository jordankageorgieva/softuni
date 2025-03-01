tabs_open = int(input())
salary = int(input())

for _ in range(tabs_open):
    site = input()
    if site == "Facebook":
        salary -= 150
        if salary == 0:
            print("You have lost your salary.")
    elif site == "Instagram":
        salary -= 100
        if salary == 0:
            print("You have lost your salary.")
    elif site == "Reddit":
        salary -= 50
        if salary == 0:
            print("You have lost your salary.")

if salary > 0:
    print(f"{salary}")