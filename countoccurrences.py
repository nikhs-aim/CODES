#  TO COUNT CHARACTERS IN A WORD OR SENTENCE
a = input('Enter a sentence: ')
count = {}

for i in a:
    count.setdefault(i, 0)
    count[i] += 1

print(count)


# HISTOGRAM
def histogram(a):
    d = dict()
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return (d)


word = input('Enter a sentence: ')
b = histogram(word)
for i in b:
    print(i, b[i])
