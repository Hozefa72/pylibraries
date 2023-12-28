list=[]
m=int(input())
for i in range(m):
    n=int(input())
    list.append(n)
max=list[0]
secmax=list[0]
for i in list:
    if(max<i):
        max=i
for j in list:
    if(max==j):
        pass
    elif(secmax<j and max>secmax):
        secmax=j
print(secmax)