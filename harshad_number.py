def sum_of_digits(num):
    sum = 0

    while (num != 0):
        last = num % 10
        sum += last
        num = num//10

    return sum


def harshad_num(num):
    sum_of_num = sum_of_digits(num)
    if num % sum_of_num == 0:
        print("harshad number")

    else:
        print("not harshad number")


harshad_num(18)
