# Problem: Min Stack
# Implement a stack that supports push, pop, and retrieving the minimum element in constant time.

from data_structures.stack import Stack


class MinStack(Stack):

    def __init__(self):
        super().__init__()  # Initialize the parent Stack
        self.min_number = Stack()  # Initialize the secondary min stack properly

    def push_to_min_stack(self, item):
        super().push(item)

        if self.min_number.is_empty() or item <= self.min_number.peek():
            self.min_number.push(item)

    def pop_from_min_stack(self):
        if self.is_empty():  # check if it is empty
            raise IndexError("Pop from an empty Stack")

        popped_item = super().pop()  # check if popped item was the current lowest value on the stack
        if popped_item == self.min_number.peek():
            self.min_number.pop()

    def __str__(self):
        parent_str_ = super().__str__()
        return f'{parent_str_}, minimum value stack: {str(self.min_number)}'


########################################
# Testing Min_Stack()
my_stack = MinStack()  # create new stack

# pushing values to stack
my_stack.push_to_min_stack(5)
my_stack.push_to_min_stack(21)
my_stack.push_to_min_stack(2)
my_stack.push_to_min_stack(1)
my_stack.push_to_min_stack(1)
my_stack.push_to_min_stack(3)
my_stack.push_to_min_stack(31)
my_stack.push_to_min_stack(341)

# Printing stack
print(my_stack)

# Popping values from stack
my_stack.pop_from_min_stack()
my_stack.pop_from_min_stack()
my_stack.pop_from_min_stack()
my_stack.pop_from_min_stack()
my_stack.pop_from_min_stack()

# Printing Stack
print(my_stack)
