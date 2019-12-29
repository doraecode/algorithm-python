A = int(input("Enter A:"))
B = int(input("Enter B:"))
def lcm(a,b):
    ma=1
    mb=1
    # conCheck = ma==mb
    while a!=b and a%b==0 and b%a==0:
        if a*ma==b*mb  or a*ma>10**5 or b*mb>10**5:
            return a*ma
        else:
            # find imposible condition
            if a*ma<b*mb :
                ma+=1
            else:
                mb+=1
    return max(a,b)
print("result : ",lcm(A,B))