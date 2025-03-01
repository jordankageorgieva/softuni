p_film = float(input())
n_persons = int(input())
p_clothes_per_person = float(input())

p_decor = p_film * 0.1

p_clothes = p_clothes_per_person * n_persons

if n_persons > 150:
    p_clothes = p_clothes - p_clothes * 0.1

p_decor_clothes = p_decor + p_clothes

if p_decor_clothes > p_film:
    print("Not enough money!")
    print(f"Wingard needs {p_decor_clothes - p_film:.02f} leva more.")
elif p_decor_clothes <= p_film:
    print("Action!")
    print(f"Wingard starts filming with {p_film - p_decor_clothes:.02f} leva left.")