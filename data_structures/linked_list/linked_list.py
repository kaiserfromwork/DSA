# Single Linked List

class SinglyNode():

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


    def __str__(self):
        return str(self.value)
 

class LinkedList():

    def __init__(self):
        self.head = None


    def append(self, value):
        if self.head is None: # first node becomes the head of the list
            head = SinglyNode(value)
            return
        
        current = self.head

        while current.next: # traverse until last node
            current = current.next

        current.next = SinglyNode(value)    # Next node will be the new node

    
    def traverse(self, head): # traverse through list (printing value of current node)
        current = head

        while current:
            print(current.value)
            current = current.next

    
