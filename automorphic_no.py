def square(num):
    return num*num


def automorphic_number(num):
    squared = square(num)

    while (num != 0):
        if num % 10 != squared % 10:
            return False
        else:
            num = num//10
            squared = squared//10

    return True


if automorphic_number(25) == True:
    print("Automorphic number")
else:
    print("Not Automorphic number")
