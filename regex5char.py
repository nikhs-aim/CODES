
# Python Program To Read Five Characters Which Start With ‘A’ And End With ‘Z’
import re
s = input("Enter the string: ")
pat = re.compile(r'^a[a-zA-Z]{3}z$')
matched = pat.search(s)
if matched != None:
    print("Search is successful")
else:
    print("Search is unsuccessful")
