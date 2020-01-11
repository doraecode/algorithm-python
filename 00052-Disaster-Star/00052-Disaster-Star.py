n = int(input(""))
for i in range(n):
    for j in range(n):
        if i+j>=(n/2)-0.5 and i-j>=-((n/2)-0.5) and i<=(n/2)-0.5 or i>(n/2)-0.5 and (i-((n/2)-0.5))-j<=0 and (i-((n/2)-0.5))+j<=n-1:
            print("*",end=" ")
        else :
            print("-",end=" ")
    print("")