n,m = [int(i) for i in input("").split()]
N = [int(i) for i in input("").split()]
result=[]
for j in range(len(N)-m+1):
    sum=0
    for k in range(j,j+m):
        if(j+m>len(N)):
            break
        else:
            sum+=N[k]
    result.append(sum/m)
print(len(result))
for i in range(len(result)):
    if((i+1)%3!=0) :
        print("%.6f"%result[i],end=" ")
    else:
        print("%.6f"%result[i])