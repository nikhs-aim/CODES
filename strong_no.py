def factorial(num):
    fact = 1
    for i in range(2, num+1):
        fact = fact*i
    return fact


def sum_of_digits(num):
    n = 0
    sum = 0
    while (num != 0):
        n = num % 10
        sum += factorial(n)
        num = num//10
    return sum


def strong_number(num):
    if sum_of_digits(num) == num:
        print("strong_number")
    else:
        print("strong_number")


strong_number(145)
