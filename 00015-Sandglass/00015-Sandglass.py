n = int(input("Enter n : "))
if n%2==0:
    print("error")
else :
    for i in range(n):
        for j in range(n):
            if(i-j<=0 and i+j<n and i<n/2 or i>n/2 and (i-j>=0 and i+j>=n-1)):
                print("*",end=" ")
            else :
                print(" ",end=" ")
        print("")
