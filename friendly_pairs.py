def sum_of_divisors(num):
    sum = 0

    for i in range(2, num+1):
        if num % i == 0:
            sum += i

    return sum


def friendly_pairs(num1, num2):
    sum1 = sum_of_divisors(num1)
    sum2 = sum_of_divisors(num2)

    a = sum1//num1
    b = sum2//num2

    print(a, b)
    if a == b:
        print("friendly pairs")

    else:
        print("not friendly pairs")


friendly_pairs(30, 140)
