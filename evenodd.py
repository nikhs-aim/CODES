# TO FIND OUT WHETHER THE GIVEN NUMBER IS EVEN OR ODD
def divides(m, n):
    if m % n == 0:
        return (True)
    else:
        return (False)


def even(n):
    return (divides(2, n))


def odd(n):
    return (not divides(2, n))


print(divides(3, 4))
print(even(5))
print(odd(7))
