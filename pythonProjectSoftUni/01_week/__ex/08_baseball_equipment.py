anual_baseball_tax = int(input())

basebal_shoes = anual_baseball_tax * (1 - 0.4)
baseball_suit = basebal_shoes * (1 - 0.2)
baseball_ball = baseball_suit * 1/4
baseball_acsesoaries = baseball_ball * 1/5

total_baseball_price = anual_baseball_tax + basebal_shoes + baseball_suit + baseball_ball + baseball_acsesoaries

print(total_baseball_price)