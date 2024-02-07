lst=['andy', 'james','Nicole','Gatsby','Matthew','David','Homer','Kane','Susindhar','Jamshed','Manpreet']
n=int(input("Enter the length"))
new_lst=[]
for item in lst:
    if(len(item)>n):
        new_lst.append(item)

print(new_lst)
