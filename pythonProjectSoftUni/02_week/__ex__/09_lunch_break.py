import math

film_name = str(input())
film_long_t = int(input())
lunch_t = int(input())

t_eat = lunch_t * 1/8
#print(f"{t_eat}")
t_sleep = lunch_t * 1/4
#print(f"{t_sleep}")
free_t = lunch_t - t_eat - t_sleep
#print(f"{free_t}")

if free_t >= film_long_t:
    print(f"You have enough time to watch {film_name} and left with {math.ceil(free_t - film_long_t)} minutes free time.")
else:
    print(f"You don't have enough time to watch {film_name}, you need {math.ceil(film_long_t - free_t)} more minutes.")