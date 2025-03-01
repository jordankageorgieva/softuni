try:
    p_kur = float(input())
    n_puzzels = int(input())
    n_dolls = int(input())
    n_bears = int(input())
    n_minions = int(input())
    n_trucks = int(input())

    p = 0.00
    n = 0
    if n_puzzels > 0:
        n = n + n_puzzels
        p = p + n_puzzels * 2.60
    if n_dolls > 0:
        n = n + n_dolls
        p = p + n_dolls * 3.00
    if n_bears > 0:
        n = n + n_bears
        p = p + n_bears * 4.10
    if n_minions > 0:
        n = n + n_minions
        p = p + n_minions * 8.20
    if n_trucks > 0:
        n = n + n_trucks
        p = p + n_trucks * 2.00

    # discount
    p_discount = 0.0
    if n >= 50:
        p_discount = p - p * 25 / 100
    else:
        p_discount = p

    # loan
    p_loan = p_discount * 10 / 100

    # end price
    p_end = p_discount - p_loan

    # if p_end != 0:
    if p_end > 0 and p_end >= p_kur:
        p_free = p_end - p_kur
        print(f"Yes! {p_free:.02f} lv left.")
    else:
        p_free = p_kur - p_end
        print(f"Not enough money! {p_free:.02f} lv needed.")
except ValueError as e:
    print(f"ValueError encountered: {e}")

