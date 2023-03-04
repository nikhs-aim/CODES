a = input('Enter:')
b = a.split()
count_letters = 0
count_words = 0
count_digits = 0
count_upper = 0
count_lower = 0

for i in a:
    count_letters += 1
    if i.isdigit():
        count_digits += 1
    if i.isupper():
        count_upper += 1
    if i.islower():
        count_lower += 1

for i in b:
    count_words += 1

print(count_letters)
print(count_words)
print(count_digits)
print(count_upper)
print(count_lower)
