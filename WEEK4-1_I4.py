b=int(input("enter the base number to find power : "))
e=int(input("enter exponent : "))
res=1
for i in range(e) :
    res=res*b
print("the result is : ",res)
