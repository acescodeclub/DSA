# A stack is basically an array with the following restrictions: 
# Data can only be inserted, read or removed from the end of the array 
# Read the reference book for more information

class Stack: 
    def __init__(self, arr=[]):
        self.stack = [*arr]
        
    # view the last item without removing it from the stack 
    def peek(self):
        return self.stack[-1]
    
    def push(self, value):
        self.stack.append(value)
        
    def pop(self): 
        return self.stack.pop()
    
    def __str__(self):
        stack = [str(i) for i in self.stack]
        return f"[{', '.join(stack)}]"
    
    def length(self):
        return len(self.stack)
    
    def isEmpty(self): 
        return len(self.stack) == 0
  
            
stack = Stack() # empty stack
print(stack.isEmpty()) # verify that it is empty

# Below are some set of actions you have performed in an IDE in their respective orders
performedActions = Stack(['write a line of code', 'write a comment', 'rename a file', 'rename a folder'])
itemsToRedo = Stack()

# So the actions you have performed are stored in memory so let us undo the the last item
# When we undo an action we put it into another stack so that we can redo it later if we want to

def undo(): 
    itemsToRedo.push(performedActions.pop())
    
def redo(): 
    performedActions.push(itemsToRedo.pop())
    
undo() 
print(f'items to redo = {itemsToRedo}  performed actions = {performedActions}')
undo()
print(f'items to redo = {itemsToRedo}  performed actions = {performedActions}')

# so If I choose to redo something I can just pop it from the redo list and put it back in the performed items

redo()
print(f'items to redo = {itemsToRedo}  performed actions = {performedActions}')





