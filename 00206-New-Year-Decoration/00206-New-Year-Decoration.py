n = int(input(""))
price=7
beautifulScore=0
count=0
while beautifulScore<n :
    count+=1
    beautifulScore+= 23
    if count%12==0 :
        beautifulScore+=98
print(price*count)