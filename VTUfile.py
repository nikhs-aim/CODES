'''Write a python program to create a folder PYTHON and under the hierarchy 3
files file1,file2 and file3.write the content in file1 as ”VTU” and in file2 as
“UNIVERSITY” and file3 content should be by opening and merge of file1 and
file2. Check out the necessary condition before write file3.'''


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
