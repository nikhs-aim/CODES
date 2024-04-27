# TO CONVERT DECIMAL TO BINARY

a = int(input('Enter a decimal number: '))
s = ''
while a > 0:
    b = a % 2
    s += str(b)
    a //= 2
print('Binary:', s[-1::-1])


def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)  # Recursive call to divide num by 2
    print(num % 2, end='')  # Prints the remainder when num is divided by 2


# Driver Code
if __name__ == '__main__':
    # decimal value
    dec_val = 7

    # Calling function
    DecimalToBinary(dec_val)
