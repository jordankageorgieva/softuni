hour_exam= int(input())
min_exam = int(input())
hour_arriving = int(input())
min_arriving = int(input())

time_exam = hour_exam * 60 + min_exam
time_arriving = hour_arriving * 60 + min_arriving

if time_arriving < time_exam - 30:
    print("Early")
elif time_exam - 30 <= time_arriving <= time_exam:
    print("On time")
elif time_arriving > time_exam:
    print("Late")

if time_arriving < time_exam:
    if time_arriving > time_exam - 60 :
        print(f"{time_exam-time_arriving} minutes before the start")
    elif time_arriving <= time_exam - 60:
        delta = time_exam - time_arriving
        hour_delta = delta // 60
        min_delta = delta % 60
        print(f"{hour_delta}:{min_delta:02d} hours before the start")
elif time_arriving > time_exam:
    if time_arriving < time_exam + 60 :
        print(f"{time_arriving - time_exam} minutes after the start")
    elif time_arriving >= time_exam + 60:
        delta = time_arriving - time_exam
        hour_delta = delta // 60
        min_delta = delta % 60
        print(f"{hour_delta}:{min_delta:02d} hours after the start")