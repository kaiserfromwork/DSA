# Double Linked List

class DoublyNode():

    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


    def __str__(self):
        return str(self.value)
    

class DoubleLinkedList():  # Double Linked List - Structuring Nodes

    def __init__(self):
        self.head = None
        self.tail = None


    # Adds Node to the end of the the List
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


    # Traverses and prints the list from head to tail
    def display_list(self):
        current = self.head
        elements = []

        while current:
            elements.append(str(current.value))
            current = current.next

        print(" <-> ".join(elements))


    # Traverses and prints the list from tail to head
    def reverse_display(self):
        current = self.tail
        elements = []

        while current:
            elements.append(str(current.value))
            current = current.prev
        
        print(" <-> ".join(elements))
    

    def search_node(self, value):
        current = self.head
        
        while current:
            if current.value == value:
                return True
            current = current.next

        return False

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