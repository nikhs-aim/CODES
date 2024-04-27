def count_digits(num):
    count = 0

    while (num != 0):
        digit = num % 10
        count += 1
        num = num//10

    return count


def power(base, exponent):
    power = 1

    for i in range(exponent):
        power = power*base

    return power


def sum_of_digits(num):
    length = count_digits(num)
    sum = 0

    while (num != 0):
        digit = num % 10
        number = power(digit, length)
        sum += number
        num = num//10

    return sum


def armstrong(num):
    if num == sum_of_digits(num):
        print("Armstrong number")
    else:
        print("Not an Armstrong number")


armstrong(153)
