list1= [1,2,3,4,5,6]
list2 = [1,2,3]

min_length = min(len(list1), len(list2))

for x,y in zip(list1[:min_length], list2[:min_length]):
    print(x,y)