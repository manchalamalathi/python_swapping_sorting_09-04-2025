# Task:- 
# program to separate odd & even elements from list 
num_list=[1,2,3,4,5,6,7,8,9,21,22,33,45,67,94,87,65,63,73]
even=[]
odd=[]
for i in num_list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even,odd)        



# program to separate unique elements from list and add "*" at EOL

num_list=[1,2,2,1,1,3,2,1,3,4,5,6,7,8,9]
unq_list=[]
star_list=[]
for i in num_list:
    if i not in unq_list:
        unq_list.append(i)
    else:
        star_list.append("*")
print(unq_list+star_list)        


