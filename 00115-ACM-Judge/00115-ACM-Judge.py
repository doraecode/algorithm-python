def wordCase(case,result):
    switcher = {
        1:'Case #'+str(case)+': Yes',
        2:'Case #'+str(case)+': No - Wrong answer',
        3:'Case #'+str(case)+': No - Time limit exceeded',
        4:'Case #'+str(case)+': No - Runtime error'
        }
    return switcher.get(result,"Invalid Case")
def checkCase():
    n = int(input("enter n : "))
    boxCase=[]
    for i in range(n):
        caseTest = input("")
        boxCase.append(caseTest)
    for i in range(len(boxCase)):
        priority = 0
        for j in range(len(boxCase[i])):
            value = boxCase[i][j]
            if value =='X' and priority<4:
                priority=4
                break
            elif value == 'T' and priority<3:
                priority=3
            elif value == '-' and priority<2:
                priority=2
            elif value == 'P' and priority<1 :
                priority=1
        print(wordCase(i+1,priority))
checkCase()

    

            
