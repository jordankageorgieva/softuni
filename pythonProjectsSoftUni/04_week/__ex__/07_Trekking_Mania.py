groups_counters = int(input())

count_total = 0
musala_gr = 0
monblan_gr = 0
kilimandjaro_gr = 0
k2_gr = 0
everest_gr = 0
for _ in range(groups_counters):
    number_peoples_in_group = int(input())
    count_total += number_peoples_in_group
    if number_peoples_in_group <= 5:
        musala_gr += number_peoples_in_group
    elif 6 <= number_peoples_in_group <= 12:
        monblan_gr += number_peoples_in_group
    elif 13 <= number_peoples_in_group <= 25:
        kilimandjaro_gr += number_peoples_in_group
    elif 26 <= number_peoples_in_group <= 40:
        k2_gr += number_peoples_in_group
    elif number_peoples_in_group >= 41:
        everest_gr += number_peoples_in_group

musala_gr_percentage = musala_gr/count_total * 100
print(f"{musala_gr_percentage:.02f}%")
monblan_gr_percentage = monblan_gr/count_total * 100
print(f"{monblan_gr_percentage:.02f}%")
kilimandjaro_gr_percentage = kilimandjaro_gr/count_total * 100
print(f"{kilimandjaro_gr_percentage:.02f}%")
k2_gr_percentage = k2_gr/count_total * 100
print(f"{k2_gr_percentage:.02f}%")
everest_gr_percentage = everest_gr/count_total * 100
print(f"{everest_gr_percentage:.02f}%")