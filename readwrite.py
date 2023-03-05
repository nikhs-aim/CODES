# TO READ THE FILE
a = open('example.txt')
b = a.read()
a.close()
print(b)

# TO READ EVERY LINE
a = open('example.txt')
b = a.readlines()
a.close()
print(b)

# TO WRITE THE FILE IN WRITE MODE
a = open('example.txt', 'w')
a.write('hello world')
a.close()

# TO WRITE THE FILE IN APPEND MODE
a = open('example.txt', 'a')
a.write('\nhii')
a.close()
