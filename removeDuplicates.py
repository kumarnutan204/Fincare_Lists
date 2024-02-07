lst=[9,3,6,32,54,45,9,54,32,6]

new_lst=[]
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
    
print(new_lst)
