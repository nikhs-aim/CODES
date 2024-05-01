def sum_proper_factors(num):
    sum = 0
    for i in range(2, num):
        if num % i == 0:
            sum += i

    return sum


def abundant_num(num):
    if sum_proper_factors(num) > num:
        print("abundant number")

    else:
        print("Not an abundant number")


abundant_num(12)
