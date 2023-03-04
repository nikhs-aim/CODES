# TO CONVERT DECIMAL TO BINARY

a = int(input('Enter a decimal number: '))
s = ''
while a > 0:
    b = a % 2
    s += str(b)
    a //= 2
print('Binary:', s[-1::-1])
