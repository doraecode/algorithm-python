input_N_M = input("Enter M , N : ")
m_n = input_N_M.split()
m = int(m_n[0])
n = int(m_n[1])
s = 65
for i in range(m):
    for j in range(n):
        if(s>89 and s>=65) or (i==0 and j==0) :
            s=65
        else :
            s+=1
        print(chr(s),end="")
    print("")