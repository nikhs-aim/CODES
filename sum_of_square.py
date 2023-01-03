#TO FIND THE SUM OF SQUARES UPTO A GIVEN NUMBER

a=int(input())
sum=0

# USING WHILE LOOP
i=1
while i<=a:
    b=a*a
    sum=sum+b
    a-=1
print(sum)


# USING FOR LOOP
for i in range(a+1):
    b=i*i
    sum+=b
print(sum)