from datetime import timedelta

exam_hour = int(input())
exam_min = int(input())

come_hour = int(input())
come_min = int(input())

time_exam = timedelta(hours=exam_hour, minutes = exam_min)
time_thirty_mins_before_exam = time_exam - timedelta(minutes=30)
time_student_arriving = timedelta(hours = come_hour, minutes = come_min)


if time_thirty_mins_before_exam <= time_student_arriving <= time_exam:
    print("On time")
    time_delta = time_exam - time_student_arriving
    one_hour = timedelta(hours = 1, minutes = 0)
    if ( (time_delta.seconds > 0 ) and (time_delta < one_hour) ):
        print(f"{(time_delta.seconds//60)%60:01d} minutes before the start")

elif time_student_arriving < time_thirty_mins_before_exam:
    print("Early")
    time_delta = time_exam - time_student_arriving
    if (time_delta < timedelta(hours = 1, minutes = 0)):
        print(f"{(time_delta.seconds//60)%60:01d} minutes before the start")
    else:
        print(f"{(time_delta.seconds//3600)}:{(time_delta.seconds//60)%60:02d} hours before the start")

elif time_student_arriving >= time_exam:
    print("Late")
    time_delta = time_student_arriving - time_exam
    if (time_delta < timedelta(hours = 1, minutes = 0)):
        print(f"{(time_delta.seconds//60)%60:01d} minutes after the start")
    else:
        print(f"{(time_delta.seconds//3600)}:{(time_delta.seconds//60)%60:02d} hours after the start")