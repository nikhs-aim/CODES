def collatz(num):
    l = []
    l.append(num)
    while (num != 1):
        if num % 2 == 0:
            num //= 2
            l.append(num)
        else:
            num = num*3+1
            l.append(num)
    print(l)


user = int(input('Enter a number: '))
collatz(user)
