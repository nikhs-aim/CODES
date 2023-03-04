def largestWord(s):
    l = s.split()
    l.sort(key=len)
    print(l[-1]+' is the longest word with length ' + str(len(l[-1])))


h = input('Enter the sentence: ')
largestWord(h)
