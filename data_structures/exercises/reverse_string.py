# Problem:
# Reverse a String – Given a string, use a stack to reverse it.

from data_structures.stack import Stack

stack = Stack()
user_string = input("Please enter a string to be reversed!")

# appending input to Stack
for char in user_string:
    stack.push(char)

# pop from stack until peek is False
while not stack.is_empty():
    print(stack.pop(), end=" ")
