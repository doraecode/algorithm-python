n = int(input(""))
arrPrice =[]
sum=0
soure=0
for i in range(n):
    Ni = int(input(""))
    if(i==0) :
        soure=Ni
    elif soure>=Ni:
        soure=Ni
    else :
        sum+=Ni-soure
        soure=Ni
print("Sum : ",sum)
