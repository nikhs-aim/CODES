a = [45, 22, 14, 65, 97, 72]
b = []
for i in a:
    if i % 3 == 0 and i % 5 == 0:
        b.append('both')
    elif i % 3 == 0:
        b.append('only 3')
    elif i % 5 == 0:
        b.append('only 5')
    else:
        b.append(i)
print(b)
