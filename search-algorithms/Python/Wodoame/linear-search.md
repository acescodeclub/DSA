Linear search, also known as sequential search, is a simple search algorithm where you iterate through a list to find a specific element. Here are a few implementations of linear search in Python:

### Iterative Linear Search:

```python
def linear_search_iterative(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the list
```

### Recursive Linear Search:

```python
def linear_search_recursive(arr, target, index=0):
    if index == len(arr):
        return -1  # Base case: element not found
    if arr[index] == target:
        return index  # Base case: element found
    return linear_search_recursive(arr, target, index + 1)
```

### Enhanced Linear Search (with Early Exit):

```python
def linear_search_early_exit(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
        elif arr[i] > target:
            break  # Early exit if the current element is greater than the target
    return -1  # Return -1 if the target is not in the list

# The list has to be sorted for this implementation
```

These are three different implementations of linear search in Python, showcasing the iterative, recursive, and enhanced approaches. Choose the one that best fits your requirements.