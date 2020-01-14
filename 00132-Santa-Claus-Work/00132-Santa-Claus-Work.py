n = int(input("enter day "))
for i in range(n):
    if i ==0 :
        gift=1+3
    else :
        gift=gift*3+gift
print(gift)