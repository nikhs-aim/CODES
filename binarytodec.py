#TO CONVERT BINARY TO DECIMAL

a=list(input('enter a binary number: '))
a.reverse()
s=0
for i in range(len(a)):
    s+=int(a[i])*2**i
print('Decimal:',s)