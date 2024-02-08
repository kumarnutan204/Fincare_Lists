lst=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40],[10,20]]
s= set()
def rem(lst):
    for item in lst:
        s.add(((tuple(sorted(item)))))
        # print(res)
    print(list(s))
    
rem(lst)
