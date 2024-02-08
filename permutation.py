import itertools

def permute(lst):
    perm=list(itertools.permutations(lst))
    print(perm)
    
a= input("Enter the list with comma separated values")
lst=(a.split(","))
permute(lst)
