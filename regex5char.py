
# Python Program To Read Five Characters Which Start With āAā And End With āZā
import re
s = input("Enter the string: ")
pat = re.compile(r'^a[a-zA-Z]{3}z$')
matched = pat.search(s)
if matched != None:
    print("Search is successful")
else:
    print("Search is unsuccessful")
