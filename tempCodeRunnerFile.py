def harshad_num(num):
    sum_of_num = sum_of_digits(num)
    if sum_of_num % num == 0:
        print("harshad number")

    else:
        print("not harshad number")


harshad_num(18)
