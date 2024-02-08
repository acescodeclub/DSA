# Suppose you are asked to check if a number exists in a large ordered list ? [1, 2, 3, ..., 155, 156, 159, ..., 500]
# You wouldn't want to search one by one since that may take a long time
# You'd rather check the middle of the list if you can; If you find the number then you've been successful ... 
# ... but if you don't, the number you get gives you more information on what to do next: for example if ... 
# .. the number is smaller than what you expected it means that your number is probably ahead in the list" [number not here | might be somwhere here ]
# Otherwise it's at the left side of the list
# You repeat this process at the required half until you obtain your number
# If the number doesn't exist in the list, then return -1.
# You can check the book for more information

def binarySearch(arr, element):
    start = 0
    end = len(arr) - 1 
    while start <= end:
        mid = (start + end) // 2 # finding the midpoint 
        if arr[mid] == element:
            return mid
        elif arr[mid] < element: 
            start = mid + 1 # Our new imaginary list begins at this index
        else: 
            end = mid - 1 # Our new imaginary list ends at this index
    return -1 # Element has not been found 

orderedArray = [1, 3, 4, 7, 8, 18, 19, 22, 27, 80, 88, 99, 100]
print(binarySearch(orderedArray, 8)) # OUPUT: 4
print(binarySearch(orderedArray, 0)) # OUTPUT: -1
        