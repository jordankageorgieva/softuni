arr1 = [1, 2, 3, 4]
arr2 = ['a', 'b']

max_len = max(len(arr1), len(arr2))

for i in range(max_len):
    x = arr1[i] if i < len(arr1) else None
    y = arr2[i] if i < len(arr2) else None
    print(x, y)
