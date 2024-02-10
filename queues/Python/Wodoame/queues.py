from collections import deque

# A queue is an array but with the following restrictions: 
# data can only be read, inserted, or removed from the beginning of the array
# You can think of it like an actual queue: people who join the queue go behind...
# ... those who are already in the queue 

class Queue: 
    def __init__(self, arr=[]):
        self.queue = deque(arr)
    
    def peek(self):
        return self.queue[0]
    
    def push(self, value):
        self.queue.appendleft(value)
        
    def pop(self): 
        self.queue.popleft()
    
    def __str__(self):
        queue = [str(i) for i in self.queue]
        return f"[{', '.join(queue)}]"
    
    def length(self):
        return len(self.queue)
    
    def isEmpty(self): 
        return len(self.queue) == 0 
    
queue = Queue()
print(queue.isEmpty()) # verify that the queue is empty
# So the queue is going to be used to keep track of some orders in a restaurant
orders = ['order 1', 'order 2', 'order 3', 'order 4', 'order 5']

# push all orders into the queue one at a time

for order in orders: 
    queue.push(order)
    
print(queue)
