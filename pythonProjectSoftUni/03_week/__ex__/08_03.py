import math
exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

total_exam_time = exam_hour * 60 + exam_minute
total_arrival_time = arrival_hour * 60 + arrival_minute

total_difference_time = abs(total_exam_time - total_arrival_time)
difference_hour = math.floor(total_difference_time // 60)
difference_minutes = total_difference_time % 60

if total_difference_time == 0:
    print("On time")

if total_exam_time > total_arrival_time and total_difference_time < 60:
    if total_difference_time <= 30:
        print("On time")
    else:
        print("Early")
    print(f"{total_difference_time} minutes before the start")

if total_exam_time > total_arrival_time and total_difference_time >= 60:
    if total_difference_time > 30:
        print("Early")
        if difference_minutes < 10:
            print(f"{difference_hour}:0{difference_minutes} hours before the start")
        else:
            print(f"{difference_hour}:{difference_minutes} hours before the start")

if total_exam_time < total_arrival_time and total_difference_time < 60:
    print("Late")
    print(f"{total_difference_time} minutes after the start")

if total_exam_time < total_arrival_time and total_difference_time > 60:
    print("Late")
    if difference_minutes < 10:
        print(f"{difference_hour}:0{difference_minutes} hours after the start")
    else:
        print(f"{difference_hour}:{difference_minutes} hours after the start")