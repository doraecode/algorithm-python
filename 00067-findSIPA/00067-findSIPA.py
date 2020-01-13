text = input("Enter word : ")
newValue = text
count=0
for i in range(len(text)):
    test=text[i:i+4]
    if len(test)<4:
        break
    if test.lower()=="sipa" :
        replaceText='"'+test+'"'
        newValue = newValue.replace(test,replaceText)
        newValue =newValue.replace('""','"')
        count+=1
print(newValue)
print(count)
