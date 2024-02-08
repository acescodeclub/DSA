A stack is a data structure that follows the Last In, First Out (LIFO) principle, meaning that the last element added to the stack is the first one to be removed. Think of it like a stack of plates where you add or remove plates from the top.

Here's a basic implementation of a stack in Python using a list:

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)
```

Explanation:

1. The `Stack` class is defined with an `__init__` method to initialize an empty list (`self.items`) to store the stack elements.

2. The `is_empty` method checks if the stack is empty.

3. The `push` method adds an item to the top of the stack by appending it to the list.

4. The `pop` method removes and returns the item from the top of the stack. It raises an `IndexError` if the stack is empty.

5. The `peek` method returns the item from the top of the stack without removing it. It also raises an `IndexError` if the stack is empty.

6. The `size` method returns the number of elements in the stack.

7. Example usage demonstrates how to create a stack, push elements onto it, pop elements off it, peek at the top element, and get the size of the stack.