list=[]
li=[]
n=int(input())
for i in range(n):
    name=input()
    marks=int(input())
    list_1=[name,marks]
    list.append(list_1)
least=None
for i in list:
    if least==None:
        least=i[1]
    elif (least>i[1]):
        least=i[1]
print(least)
secleast=None
for i in list:
    if(least==i[1]):
        pass
    elif(secleast==None):
        secleast=i[1]
    elif(secleast>least and secleast>i[1]):
        secleast=i[1]
    if(secleast==i[1]):
        li.append(i[0])
for i in li:
    print(i)
    
