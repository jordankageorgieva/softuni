bee_plus = [32, 42, 7, 28, 3]

bee_minus = [1 ,5, 6]

bee_minus_minus = 0
for bee_index in range(0, len(bee_plus)):
     bee = bee_plus[bee_index]
     print("current bee ", bee)
     print("bee_minus_minus ", bee_minus_minus)
     if bee_minus_minus == 0:
        bee_kill = bee_minus[len(bee_minus) -1] * 7
        print("current bee killed ", bee_kill)
     else:
         bee_kill = bee_minus[len(bee_minus) - bee_index - 1]
         print("current bee killed ", bee_kill)

     if bee > bee_kill:
         pass
     elif bee < bee_kill:
         bee_minus_minus = bee_minus[len(bee_minus) - bee_index -1] - bee % 7
         bee_minus[len(bee_minus) - bee_index -1] = bee_minus_minus
     elif bee_plus == bee_kill:
         pass