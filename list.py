string=input("Enter a stirng")
lower=0
upper=0
alpha=0
digit=0
for a in string:
    if(a.islower()):
        lower=lower+1
    elif(a.isupper()):
        upper=upper+1
    if a.isalpha():
        alpha=alpha+1
    if a.isdigit():
        digit=digit+1
print("No of upperacse words",upper)
print("No of lowercase words",lower)
print("No of alpabetic words",alpha)
print("No  of digit",digit)