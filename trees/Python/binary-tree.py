# This class defines the nodes that make up a binary tree
# A node has a value it stores
# A node may have a left child and a right child
class TreeNode:
    def __init__(self, value, leftChild=None, rightChild=None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
    
    def __str__(self) -> str:
        return f"<TreeNode:{self.value}>"

# This class defines the binary tree
class BinaryTree: 
    def __init__(self, root=None): # The tree can be initialized with a root otherwise the root is 'None'
        self.root  = root
         
    def search(self, value): 
        def inner(value, node):
            if not node or node.value == value: 
                return node
            elif value < node.value: 
                return inner(value, node.leftChild)
            else:
                return inner(value, node.rightChild)
        return inner(value, self.root)
        
    
    def insert(self, value): 
        def inner(value, node):
            if value < node.value: 
                if not node.leftChild: 
                    node.leftChild = TreeNode(value)
                else: 
                    inner(value, node.leftChild)
            elif value > node.value: 
                if not node.rightChild:
                    node.rightChild = TreeNode(value) 
                else: 
                    inner(value, node.rightChild)
                    
        if not self.root: # we create a root if the tree is empty
            self.root = TreeNode(value)
        else: 
            inner(value, self.root)
    
    # both inorder and reverse traversal supported
    def traverse(self, reverse=False): 
        def forward(node: TreeNode): 
            if not node: 
                return 
            
            forward(node.leftChild)
            print(node)
            forward(node.rightChild)
            
        def backward(node: TreeNode): 
            if not node: 
                return 
            backward(node.rightChild)
            print(node)
            backward(node.leftChild)
        
        if not reverse:  
            forward(self.root)
        else:
            backward(self.root)
    
    def isEmpty(self): # the tree must have at least one node (the root) otherwise it is empty
        return self.root is None 
         
                    
tree = BinaryTree() # an empty binary tree
print(tree.isEmpty()) # verify that it is empty
print()

tree.insert(20)
tree.insert(30)
tree.insert(15)
tree.insert(72)
tree.insert(48)

tree.traverse()
print() 
tree.traverse(reverse=True)
print() 

books = BinaryTree()
books.insert("Moby Dick")
books.insert("Great Expectations")
books.insert("Robinson Crusoe")
books.insert("Alice in Wonderland")
books.insert("Lord of the Flies")
books.insert("Pride and Prejudice")
books.insert("The Odyssey")

books.traverse() # alphabetical order of book titles
