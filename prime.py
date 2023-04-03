#  FIND FACTORS
def factors(n):
    fl = []
    for i in range(1, n+1):
        if n % i == 0:
            fl += [i]
    return (fl)


#  FIND IF THE NUMBER IS PRIME OR NOT
def isprime(n):
    return (factors(n) == [1, n])


# TO FIND OUT PRIME NUMBERS UPTO A RANGE
def primesupto(n):
    primelist = []
    for i in range(1, n+1):
        if isprime(i):
            primelist += [i]
    return (primelist)


#  TO LIST FIRST N PRIME NUMBERS
def nprimes(n):
    (count, i, plist) = (0, 1, [])
    while (count < n):
        if isprime(i):
            (count, plist) = (count+1, plist+[i])
        i += 1
    return (plist)


b = int(input('Enter a number: '))
print(isprime(b))
print(primesupto(b))
print(nprimes(b))
