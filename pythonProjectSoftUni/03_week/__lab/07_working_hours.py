hour= float(input())
week_day = str(input())

if week_day in ["Monday", "Tuesday","Wednesday","Thursday","Friday", "Saturday"] and 10.00 <= hour <= 18.00:
    print("open")
else:
    print("closed")