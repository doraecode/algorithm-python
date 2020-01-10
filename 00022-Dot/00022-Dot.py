n = int(input("enter n: "))
box=[]
for i in range(n):
    xy=input("enter x,y : ")
    text_xy=xy.split()
    if text_xy[0] in box :
        box.remove(text_xy[0])
    else :
        box.append(text_xy[0])

    if text_xy[1] in box :
        box.remove(text_xy[1])
    else :
        box.append(text_xy[1])
print("result : ",len(box))

