# TO REPLACE ZEROES WITH ONES AND ONES WITH ZEROES

a = ''
user = input('enter a number: ')
for i in user:
    if i == '0':
        a += '1'
    if i == '1':
        a += '0'
print('Replaced: ', a)
