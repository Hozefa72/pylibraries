a=('a','p','p','l','e')
b=input("enter a character from apple")
if b in a:
    count=0
    for i in a:
        if i!=b:
            count+=1
        else: 
            break
    print("The Character",b," is at index",count)
else:
    print("The charcter ",b,"is not in tuple")