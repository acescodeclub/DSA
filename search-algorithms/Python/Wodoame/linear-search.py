# To search linearly means checking each element one by one until the target element is found
# In this case we are going to find the index of the element if it exists or -1 otherwise

def linearSearch(arr, targetElement):
    for i in range(len(arr)): 
        element = arr[i]
        if element == targetElement: 
            return i # return the index of the element (or better still the first occurrence of the element) if it exists
    return -1  # Element has not been found therefore we return -1

arr = [1, 3, 4, 5, 1, 1]
print(linearSearch(arr, 5)) # OUTPUT: 3
print(linearSearch(arr, 6)) # OUTPUT: -1

    