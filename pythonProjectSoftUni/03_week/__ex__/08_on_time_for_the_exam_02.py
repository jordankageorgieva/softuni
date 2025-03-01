hour_exam = int(input())
min_exam = int(input())
hour_arrival = int(input())
min_arrival = int(input())

time_exam = (hour_exam * 60) + min_exam
time_arrival = (hour_arrival * 60) + min_arrival
time_diff = time_exam - time_arrival

if time_diff > 30 :
    print('Early')
elif time_diff < 0 :
    print('Late')
else :
    print('On time')

hours = abs(time_diff) // 60
min = abs(time_diff) % 60

result = ''

if hours > 0 :
    result += f'{hours}:{min:02d} hours'
elif min > 0 :
    result += f'{min} minutes'
if time_diff > 0 :
    result += f' before the start'
elif time_diff < 0 :
    result += f' after the start'

print(result)