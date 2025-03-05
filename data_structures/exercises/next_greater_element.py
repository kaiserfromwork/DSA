# Problem
# For each element in an array, find the next greater element on the right.
import random
from data_structures.stack import Stack

numbers_dict = {
    1: [342, 78, 901, 453, 627, 215, 984, 512, 699, 134],
    2: [23, 876, 432, 990, 156, 789, 567, 321, 654, 891, 234, 678, 987, 543, 100],
    3: [456, 789, 123, 987, 234, 876, 345, 765, 678, 432],
    4: [876, 543, 321, 987, 654, 210, 789, 456, 123, 1000, 345, 567],
    5: [999, 888, 777, 666, 555, 444, 333, 222, 111, 112, 113, 114],
    6: [147, 258, 369, 159, 753, 852, 951, 357, 951, 456],
    7: [111, 222, 333, 444, 555, 666, 777, 888, 999, 1000, 101, 202],
    8: [512, 345, 678, 123, 789, 234, 890, 567, 901, 210],
    9: [102, 304, 506, 708, 910, 112, 314, 516, 718, 920],
    10: [999, 100, 222, 333, 444, 555, 888, 777, 666, 111, 200, 300, 400]
}


def next_greater_number(my_list):
    my_stack = Stack()
    result = [-1 for x in range(0, len(my_list))]
    if len(my_list) == 0:
        print("INVALID LIST")
    else:
        for index, number in enumerate(my_list):  # Using enumerate to better keep track of indexes
            while not my_stack.is_empty() and number > my_list[my_stack.peek()]:  # Check if stack is not empty and compare current number to index number on top of stack
                popped_index = my_stack.pop()  # using index on top of stack to update number
                result[popped_index] = number
            my_stack.push(index)  # keeping track of indexes with Stack
    return result


number_list = numbers_dict[random.randint(1, len(numbers_dict))]
print(f'{next_greater_number(number_list)} is the greatest number in {number_list}')

