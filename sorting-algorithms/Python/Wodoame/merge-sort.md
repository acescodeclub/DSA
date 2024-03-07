# Visualization of merge sort
Click the link to go to the video

[![merge sort visualization](https://img.youtube.com/vi/5Z9dn2WTg9o/0.jpg)](https://www.youtube.com/watch?v=5Z9dn2WTg9o)

Merge sort is a popular sorting algorithm that follows the divide-and-conquer paradigm. Here's a simple implementation of merge sort in Python:

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively divide the array into two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        merge(arr, left_half, right_half)

def merge(arr, left, right):
    i = j = k = 0

    # Compare and merge the elements from left and right arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Check for any remaining elements in left and right arrays
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
```

This implementation defines a `merge_sort` function that recursively divides the array into two halves and calls the `merge` function to merge the sorted halves. The `merge` function compares elements from the left and right halves and merges them into the original array. The example usage demonstrates sorting an array using this merge sort implementation.

This is another reference to help you understand better

[![merge sort visualization and implementation in python](https://img.youtube.com/vi/cVZMah9kEjI/0.jpg)](https://www.youtube.com/watch?v=cVZMah9kEjI)