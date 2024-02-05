# We want to sort a list of numbers in ascending order. For example [5, 2, 0, 4, 3]
# We compare the first element to the second element
# If it's larger then we swap their positions because we want an ascending order: [2, 5, 0, 4, 3]
# Now we move to the next position and do the same thing: [2, 0, 5, 4, 3]
# Notice the progression of the largest element to the end of the list
# After the first pass through the largest element will be in the correct position ...
# ... so we don't need worry about it again: [2, 0, 4, 3, 5]
# we continue the process ( n - 1 more times ) until the list is completely sorted
# Check the book in the repository for more visual information 

def bubbleSort(arr):
    n = len(arr)
    sortUntil = n - 1 # elements beyond this index are already sorted
    # outer loop repeats the main process n times
    for i in range(n):
        # main process
        for j in range(sortUntil): 
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # swap operation
                
        # after every pass through an element ends up in the correct position towards the end
        print(f'pass through = {i + 1}; array = {arr}; elements from index {sortUntil} are already sorted')
        sortUntil -= 1
    return arr

print(bubbleSort([5, 2, 0, 4, 3]))

            
