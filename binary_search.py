def binary_search(array, item,mid1=0):
    mid = len(array)//2
    mid1 = mid1 + len(array)//2
    if array[mid]==item:
        return mid1
    elif array[mid]>item:
        return binary_search(array[0:mid], item)
    else:
        return binary_search(array[mid:],item,mid1)

a=[1,2,3,4,5,6]
print(binary_search(a,1))
print(binary_search(a,2))
print(binary_search(a,3))
print(binary_search(a,4))
print(binary_search(a,5))
print(binary_search(a,6))