class Stack:  # LIFO - Last In First Out

    def __init__(self):  # create an empty list
        self.stack = []

    def push(self, item):  # append item to end of list
        self.stack.append(item)

    def pop(self):  # remove last item of the list
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def peek(self):  # return value of the last item of the list
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):  # check if the Stack is empty
        return len(self.stack) == 0

    def size(self):  # check the size of Stack
        return len(self.stack)
