A = [int(i) for i in input("").split()]
B = [int(i) for i in input("").split()]
for i in range(len(A)):
    if(i==0 ) :
        minA= A[i]
    elif A[i]<minA:
        minA= A[i]
    for j in range(len(A)):
        if i==0 and j==1:
            sumMinA=A[i]+A[j]
        elif i!=j and A[i]+A[j]<sumMinA:
            sumMinA=A[i]+A[j]
for i in range(len(B)):
    if(i==0 ) :
        minB= B[i]
    elif B[i]<minB:
        minB= B[i]
    for j in range(len(B)):
        if i==0 and j==1:
            sumMinB=B[i]+B[j]
        elif i!=j and B[i]+B[j]<sumMinB:
            sumMinB=B[i]+B[j]
bothStore=minA+minB+100
if sumMinA<=sumMinB and sumMinA<=bothStore:
    print(sumMinA)
elif sumMinA>sumMinB and sumMinB<=bothStore:
    print(sumMinB)
else:
    print(bothStore)
