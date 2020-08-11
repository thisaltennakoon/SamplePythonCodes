def binary_search(array,item,index=0):
    array_size=len(array)
    if array_size==0:
        return -1
    elif array_size==1 :
        if array[0]==item:
            return 0
        else:
            return -1
    else:
        mid=array_size//2
        index=index+mid
        if array[mid]==item:
            return index
        elif array[mid]>item:
            return f(array[0:mid],item)
        else:
            return f(array[mid:], item, index)
a=[1,2,3,4,5,6,7,8,9]
print(f(a,0))
print(f(a,1))
print(f(a,2))
print(f(a,9))
