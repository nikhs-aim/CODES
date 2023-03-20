# OUTPUTS THE STEPS IN CACULATING THE GCD
def gcd(m, n):
    if m < n:
        (m, n) = (n, m)
    while m % n != 0:
        diff = m-n
        (m, n) = (max(n, diff), min(n, diff))
        print(m, n)
    return n


a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
gcd(a, b)


# ACTUAL EUCLID'S ALGORITHM
def gcd(m, n):
    if m < n:
        (m, n) = (n, m)
    while m % n != 0:
        (m, n) = (n, m % n)
    return n


a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
print(gcd(a, b))


def f(x):
    d = 0
    y = 1
    while y <= x:
        d = d+1
        y = y*3
    print(d)


f(2343)
