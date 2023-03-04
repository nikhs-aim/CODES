# FIND THE GCD  - 1

def gcd(m, n):
    fm = []
    fn = []
    cf = []

    for i in range(1, m+1):
        if (m % i) == 0:
            fm.append(i)

    for i in range(1, n+1):
        if (n % i) == 0:
            fn.append(i)

    for f in fm:
        if f in fn:
            cf.append(f)

    return cf[-1]


m = int(input('first: '))
n = int(input('second: '))
print('The gcd is: ', gcd(m, n))


# FIND THE GCD  - 2

def gcd(m, n):
    cf = []
    for i in range(1, min(m, n)+1):
        if (m % i) == 0 and (n % i) == 0:
            cf.append(i)
    print(cf[-1])


m = int(input('First: '))
n = int(input('Second: '))
gcd(m, n)


# FIND THE GCD  - 3 (without using lists to store all the factors)

def gcd(m, n):
    for i in range(1, min(m, n)+1):
        if (m % i) == 0 and (n % i) == 0:
            mrcf = i       # each time assign obtained common factor
    print(mrcf)


m = int(input('First: '))
n = int(input('Second: '))
gcd(m, n)


# FIND THE GCD  - 4 (get the gcd by scanning backwards i.e from min(m,n))

def gcd(m, n):
    i = min(m, n)
    while i > 0:
        if (m % i) == 0 and (n % i) == 0:
            print(i)
            break
        else:
            i -= 1


m = int(input('First: '))
n = int(input('Second: '))
gcd(m, n)
