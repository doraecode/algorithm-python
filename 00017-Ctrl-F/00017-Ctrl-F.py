test = input(" n,m :")
number = test.split()
n = input("enter word n: ")
m = input("enter word m: ")
num_n= int(number[0])
num_m= int(number[1])

word_n = n.lower()[:num_n]
word_m = m.lower()[:int(num_m)]
count=0
for i in range(num_n):
    if i+1<=num_n:
        nextPt=i+num_m
    if(word_n[i:nextPt]==word_m):
        count+=1
print("result : ",count)
# should check input == n and m 