t = int(input("enter T : "))
for i in range(t):
    x,y,z = [int(j) for j in input("").split()]
    if x!=0 and y!=0 and z!=0 :
        print("YES")
    elif (x==1 and y>=1 or (y==1 and z>=1) )or (z==1 and x>=1):
        print("YES")
    else:
        print("NO")