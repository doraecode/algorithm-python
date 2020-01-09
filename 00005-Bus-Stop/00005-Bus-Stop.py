n = int(input("number of bus :"))
box =[]
for i in range(n):
    time = int(input("Time of travel :"))
    box.append(time)
mulbox =1
mul = 2
while mul<=max(box) :
    check= True
    for i in range(len(box)) :
        if box[i]%mul==0 :
            box[i]=box[i]/mul
            if check==True:
                check=False
                mulbox*=mul
    if check ==True :
        mul+=1
    else :
        mul=2
print("result : ",mulbox)
