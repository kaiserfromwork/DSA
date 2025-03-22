# Double Linked List

class DoublyNode():


    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


    def __str__(self):
        return f"{self.value, self.next, self.value}"
    

class DoubleLinkedList():


    def __init__(self):
        self.head = None


    def append(self, value):
        if self.head is None:
            self.head = DoubleLinkedList(value)
            return
        
        current = self.head
        while current.next:
            pass