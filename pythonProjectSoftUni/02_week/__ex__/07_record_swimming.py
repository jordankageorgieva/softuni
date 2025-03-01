import math

best_record_sec_input = float(input())
distance_m_input = float(input())
current_time_s_input = float(input())

current_time_for_record = distance_m_input * current_time_s_input

time_resistance_water = math.floor(distance_m_input / 15) * 12.5

current_time_total_record = current_time_for_record + time_resistance_water

if best_record_sec_input > current_time_total_record :
    print(f"Yes, he succeeded! The new world record is {current_time_total_record:.02f} seconds.")
else:
    print(f"No, he failed! He was {current_time_total_record - best_record_sec_input:.02f} seconds slower.")