# Double Linked List

class DoublyNode():

    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


    def __str__(self):
        return str(self.value)
    

class DoubleLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, value):
        if self.head is None:
            self.head = DoublyNode(value)
            self.tail = self.head
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = DoublyNode(value, prev=current)
        self.tail = current.next


    def display_list(self):
        current = self.head
        elements = []

        while current:
            elements.append(str(current.value))
            current = current.next

        print(" <-> ".join(elements))

    def reverse_display(self):
        current = self.tail
        elements = []

        while current:
            elements.append(str(current.value))
            current = current.prev
        
        print(" <-> ".join(elements))


########################### TEST ###########################

db_node = DoublyNode(5)
print(f"Single Print First Node: {db_node}")

db_list = DoubleLinkedList()

db_list.append(5) 
db_list.display_list()

db_list.append(25)
db_list.append(22)
db_list.append(32)

print("Adding more nodes!")
db_list.display_list()

print("Reverse List")
db_list.reverse_display()