box = []
n = int(input("enter N :")) 
for i in range(n) :
    hi = int(input("enter Hi :"))
    box.append(hi)
check = False  
mini = min(box)
while check==False :
    for i in box:
        if i%mini!=0:
            check = False
            mini-=1
            break
        else :
            check=True
sum=0
for i in box:
    sum+=i/mini
print("Sum box to use : ",sum)
