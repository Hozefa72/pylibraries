list_1=['a','b','c']
list_2=['h','i','t']
list_3=['0','1','2']
print("The original list is")
print(list_1)
print(list_2)
print(list_3)
for i in range(len(list_3)):
    list_1.insert(i,list_3[i])
for j in list_2:
    list_1.append(j)
print(list_1)
