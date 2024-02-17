# A linked list is a collection of nodes 
# nodes are objects that contain some data 
# Each node is connected to another node so linked lists do not ...
# ... require a contiguous section of memory like an array
# read the reference book for more information
# Let's start by creating a node that will contain data

class Node: 
    def __init__(self, data):
        self.data = data
        self.nextNode = None


node = Node('hello') # creating a node
print(node.data) # verify that it contains that data 'helo'
print(node.nextNode) # It doesn't point to any other node

# So a linked list is basically a collection of nodes
# This is a basic implementation of a linked list
class LinkedList: 
    def __init__(self, firstNode):
        self.firstNode = firstNode
        # we need a first node to indicate the starting point of the linked list 
        # Every node then knows it's other nodes which will make traversal of the list possible
        
    def get(self, index): 
        currentIndex = 0
        currentNode = self.firstNode
        while currentIndex < index: 
            currentNode = currentNode.nextNode
            currentIndex += 1
        return currentNode.data
    
    def insert(self, value, index): 
        newNode = Node(value) # create a new node
        currentIndex = 0
        currentNode = self.firstNode
        while currentIndex < index - 1: # insert it between index - 1  and the desired index (print the list to see what I mean)
            currentNode = currentNode.nextNode
            currentIndex += 1
        newNode.nextNode = currentNode.nextNode
        currentNode.nextNode = newNode
    
    def search(self, value):
        currentIndex = 0
        currentNode = self.firstNode
        while currentNode: 
            if currentNode.data == value: 
                return currentIndex
            
            currentNode = currentNode.nextNode
            currentIndex += 1
        return -1
    
    def remove(self, index):
        if index == 0: 
            self.firstNode = self.firstNode.nextNode
        else: 
            currentIndex = 0 
            currentNode = self.firstNode
            while currentIndex < index - 1: 
                currentNode = currentNode.nextNode
                currentIndex += 1
            currentNode.nextNode = currentNode.nextNode.nextNode 
        # we have removed the link between the node to delete and it's previous node
        # Such that the previous node just links to the node after the node to delete
    
    
    # overriding the print() function to display the linked list
    # You may choose to implement a display() method for that purpose instead
    def __str__(self): 
        strResult = '['
        currentNode = self.firstNode
        while currentNode: 
            strResult += str(currentNode.data) + ', '
            currentNode = currentNode.nextNode
        strResult = strResult.removesuffix(', ') + ']'
        return strResult


node1 = Node('I')
node2 = Node('am')
node3 = Node('happy')
node4 = Node('today')

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

linkedList = LinkedList(node1)
print(linkedList.get(2))
print(linkedList)
linkedList.insert('very', 2)
print(linkedList)
print(linkedList.search('today'))
print(linkedList.remove(2))
print(linkedList)
