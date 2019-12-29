A = int(input("Enter A:"))
B = int(input("Enter B:"))
def gcd(a,b):
    min=0
    if a<b:
        min=a
    else:
        min=b
    conCheck = a%min==0 and b%min==0 and min>0
    first = True
    while conCheck==False:
        if a%min==0 and b%min==0 or min<0:
            return min
        else:
            if first and min%2==0:
                first =False
                min/=2
            else :
                min-=1
    return min
# should not prime number 
print("result : ",gcd(A,B))