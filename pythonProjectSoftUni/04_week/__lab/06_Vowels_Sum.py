text = str(input())

value = 0
for index in range(0, len(text)):
    if text[index] == 'a':
        value += 1
    elif text[index] == 'e':
        value += 2
    elif text[index] == 'i':
        value += 3
    elif text[index] == 'o':
        value += 4
    elif text[index] == 'u':
        value += 5

print(value)