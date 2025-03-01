sportist_time_one = int(input())
sportist_time_two = int(input())
sportist_time_three = int(input())

sportist_time_sum = sportist_time_one + sportist_time_two + sportist_time_three

# all the seconds to be converted to minutes and seconds
sportist_time_minutes = sportist_time_sum // 60
sportist_time_seconds = sportist_time_sum % 60

if sportist_time_seconds < 10:
    print(f"{sportist_time_minutes}:{sportist_time_seconds:02d}")
else:
    print(f"{sportist_time_minutes}:{sportist_time_seconds}")