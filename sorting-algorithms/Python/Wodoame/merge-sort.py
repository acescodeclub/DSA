# NOTE: This algorithm uses recursion so you have to understand how to read recursive code

def mergeSort(arr):
    # we split the array if it has more than one element
    if len(arr) > 1: 
        # we obtain the middle index and split the array into two parts (left and right)
        mid = len(arr) // 2
        leftArray = arr[:mid]
        rightArray = arr[mid:]
        
        mergeSort(leftArray) # we call the function again to split the left array into two parts as well
        mergeSort(rightArray) # we call the function again to split the right array into two parts as well
    
        # merge step (watch the second video using the link in the .md files to understand the below code)
        # The merge step is basically combining the two halves into a single sorted array
        
        i = 0 
        j = 0 
        k = 0 # used to overwrite the input array but this time in a sorted order
        while i < len(leftArray) and j < len(rightArray): 
            if leftArray[i] <= rightArray[j]: 
                arr[k] = leftArray[i]
                i += 1 
            else: 
                arr[k] = rightArray[j]
                j += 1 
            k += 1
        
        if i < len(leftArray): 
            arr[k:] = leftArray[i:]
        elif j < len(rightArray): 
            arr[k:] = rightArray[j:]
        return arr # array is sorted in place and we really do not need this line 
    
array = [18, 12, 11, 10, 5, 1, 2, 6, 7]
print(f'original array = {array}')
print(f'sorted array = {mergeSort(array)}')
