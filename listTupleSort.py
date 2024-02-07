lst=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(n):
    return n[-1]

def sort(lst):
    return sorted(lst,key=last)

print("sorted: ")
print(sort(lst))
