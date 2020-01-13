n = int(input("enter n : "))
cube = input(" color cube : ")
temp=''
for i in range(len(cube)) :
    if(cube[i]==temp and i!=0):
        print('Wrong Answer')
        break
    else :
        if i==len(cube)-1 :
            print("Accepted")
        temp=cube[i]
        
       