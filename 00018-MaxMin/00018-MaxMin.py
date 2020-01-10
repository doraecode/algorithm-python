n = int(input("enter n : "))
for i in range(n):
    k = int(input())
    if(i==0):
        min=k
        max=k
    elif k<min:
        min=k
    elif k>max:
        max=k
print("max : ",max)
print("min : ",min)
