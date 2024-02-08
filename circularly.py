l1=[1,2,3,4,5,6,83]
l2=[7,3,4,6,8,9,0,67]
def circular(l1,l2):
    print(f"For the given lists cicularity is: ")
    print(' '.join(map(str, l2)) in ' '.join(map(str, l1 * 2)))

circular(l1,l2)
