p_kur = float(input())

n_puzzels = int(input())
n_dolls = int(input())
n_bears = int(input())
n_minions = int(input())
n_trucks = int(input())

n_toys = n_puzzels + n_dolls + n_bears + n_minions + n_trucks

p = ((n_puzzels * 2.60) + (n_dolls * 3) + (n_bears * 4.1) + (n_minions * 8.2) + (n_trucks * 2))

if n_toys >= 50:
    p = p - p * 25 / 100

# without loan
p = p - p * 10 / 100

if p >= p_kur:
    print(f"Yes! {p - p_kur:.02f} lv left.")
else:
    print(f"Not enough money! {p_kur - p:.02f} lv needed.")
