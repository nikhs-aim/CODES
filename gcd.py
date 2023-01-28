# FIND THE GCD 



def gcd(m,n):
   fm=[]
   fn=[]
   cf=[]

   for i in range(1,m+1):
    if (m%i)==0:
        fm.append(i)

   for i in range(1,n+1):
    if (n%i)==0:
        fn.append(i)

   for f in fm:
    if f in fn:
        cf.append(f)

   return cf[-1]



m=int(input('first: '))
n=int(input('second: '))
print('The gcd is: ',gcd(m,n))