x = int(input("enter rate A : "))
n = input("enter score : ")
inputN = n.split()
sum=0
for i in inputN:
    sum+=int(i)
# sum>inputN
cando = False
if(sum==x):
    for i in inputN:
        print(i,end=" ")
else :
    for i in range(len(inputN)):
        if sum-int(inputN[i])==x:
            inputN[i]='0'
            cando=True
            break
    if cando:
        for i in inputN:
            print(i,end=" ")
    else:
        print('-1')
