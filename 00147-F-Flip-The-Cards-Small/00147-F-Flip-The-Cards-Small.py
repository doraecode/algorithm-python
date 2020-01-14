n,m = [int(i) for i in input("").split()]
turnup=[]
fold =[]

for i in range(n):
    faceup,folded = [int(i) for i in input("").split()]
    turnup.append(faceup)
    fold.append(folded)
for i in range(m):
    switch = int(input(""))
    for j in range(len(turnup)):
        if(switch>=turnup[j]) :
            temp=turnup[j]
            turnup[j]=fold[j]
            fold[j]=temp
print("Output")
for i in turnup:
    print(i)
