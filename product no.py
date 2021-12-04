num=int(input("enter the number"))
i=1
product=1
while num>0:
    rem=num%10
    product=product*rem
    num=num//10
    print("product of digit=",product) 
     
