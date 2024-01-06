# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class Linked List
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Check the Size of the Linked List    
    def listLen(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.next
            count += 1
        return count               

    def insertHead(self, headNode):
        tempNode = self.head # Stores Previous Chain 
        self.head = headNode # Assigns a new Head Node
        headNode.next = tempNode # Assigns previous chain to New head Node
        del tempNode # Delets the Temp. Node to save Space
    
    # Insert Node a position
    def insertAt(self, newNode, position):
        # Checks if the postion is valid if not then returns an error message
        if position < 0 or position > self.listLen:
            print("Invalid Position")
            return
        
        # Insert Node as head if the postion is 0
        if position == 0:
            self.insertHead(newNode)
            return
        
        currentNode = self.head
        currentPostition = 0
        while True:
            if currentPostition == position: 
                previousNode.next = newNode # Links before Current Node chain to new Node
                newNode.new = currentNode # Links New Node to after Current Node Chain 
                break
            previousNode = currentNode # Stores before Current Node chain
            currentNode = currentNode.next # Stores after Current Node chain
            currentPostition += 1
    
    # To Insert values into Linked List
    def insertEnd(self, newNode):
        # To check is head Node is Empty if emtry then assigns a Head Node
        if self.head is None:
            self.head = newNode 
        else:
            lastNode = self.head 
            while True: # Finds the Last Node in the linked list
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode 
    
    # To Print linked List
    def printList(self): 
        if self.head is None: 
            print("Linked list is empty")
            return
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next



# Creates a Linked List 
linkedList = LinkedList()

# Creating Nodes and inserting to end of Linked List
n1 = Node('New Delhi')
linkedList.insertEnd(n1)
n2 = Node('San Francisco')
linkedList.insertEnd(n2)
n3 = Node('London')
linkedList.insertEnd(n3)
n4 = Node('Tokyo')
linkedList.insertEnd(n4)
n5 = Node('Kathmandu')
linkedList.insertEnd(n5)

# Assigns a new Head Node
h1 = Node('Mumbai')
linkedList.insertHead(h1)

# Printing Linked List
linkedList.printList()
