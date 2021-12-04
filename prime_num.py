num=int(input("enter the number"))
i=2
j=0
a=num/2
while i<=a:
    if num%i==0:
        j=1
        break
    i=i+1
if j==0:
    print("it is prime number")
else:
    print("not a prime")
