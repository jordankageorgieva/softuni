deposit_sum = float(input())
# if (deposit_sum<100.00 and deposit_sum > 10000.00):
#     print("NOT CORRECT DEPOSIT SUM")

deposit_deadline = int(input())
interest_rate = float(input())

annual_interest_rate = interest_rate/100
interest_rate_per_one_annual = deposit_sum*annual_interest_rate
interest_rate_per_month = interest_rate_per_one_annual/12
total_interest_rate_per_period = deposit_sum + interest_rate_per_month*deposit_deadline

print(total_interest_rate_per_period)
