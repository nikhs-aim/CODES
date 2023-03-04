a = input('Enter a sentence: ')
count = {}

for i in a:
    count.setdefault(i, 0)
    count[i] += 1

print(count)
