a = input('Enter a word: ')
list = []
for i in a:
    if i.isupper():
        list.append(i.lower())
    if i.islower():
        list.append(i.upper())
result = ''.join(list)
print(result)
