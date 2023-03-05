import os

folder_path = './PYTHON'
os.makedirs(folder_path)


file1_path = './PYTHON/file1'
a = open(file1_path, 'w')
a.write('VTU')
a.close()

file2_path = './PYTHON/file2'
b = open(file2_path, 'w')
b.write('UNIVERSITY')
b.close()

file3_path = './PYTHON/file3'
c = open(file1_path, 'r')
d = open(file2_path, 'r')
e = open(file3_path, 'w')
content = c.read() + d.read()
e.write(content)
