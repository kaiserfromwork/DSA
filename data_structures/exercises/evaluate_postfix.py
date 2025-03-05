# Problem
# Evaluate Postfix Expression – Given a postfix mathematical expression, evaluate its result using a stack.

from data_structures.stack import Stack
import random

postfix_expressions = [
    ("3 4 +", 7),       # 3 + 4 = 7
    ("5 1 2 + 4 * + 3 -", 14),  # 5 + ((1 + 2) * 4) - 3 = 14
    ("2 3 * 5 4 * +", 26),  # (2 * 3) + (5 * 4) = 26
    ("8 2 / 3 -", 1),  # (8 / 2) - 3 = 1
    ("7 8 + 3 2 + /", 3),  # (7 + 8) / (3 + 2) = 3
    ("9 3 1 - *", 18),  # 9 * (3 - 1) = 18
    ("6 2 / 3 *", 9),  # (6 / 2) * 3 = 9
    ("10 2 8 * + 3 -", 23),  # (10 + (2 * 8)) - 3 = 23
    ("4 2 + 3 5 1 - * +", 18),  # (4 + 2) + (3 * (5 - 1)) = 19
    ("7 2 3 + * 5 /", 7),  # (7 * (2 + 3)) / 5 = 7
]

math_symbols = ['+', '-', '*', '/']  # used to differentiate between numbers/space in expression
numbers_stack = Stack()  # initiating stack

# picking random expression. also storing answer of expression for testing for later
expression, answer = postfix_expressions[random.randint(0, len(postfix_expressions) - 1)]  #


def eval_postfix(math_expression):
    result = []
    for char in math_expression:
        if char not in math_symbols:  # Pushing "numbers" and spaces to stack, spaces help to figure out what is being calculated together
            numbers_stack.push(char)
        else:
            counter = 0
            numbers_stack.pop()  # popping space
            while counter < 2:
                if numbers_stack.is_empty():  # break loop if no items left on the stack
                    break
                if numbers_stack.peek() == " ":  # using blank spaces to calculate
                    counter += 1
                    if counter < 2:
                        result.append(char)  # first space is replaced by math symbol (+, -, *, /), the popped
                        numbers_stack.pop()
                else:
                    # adding number to list to create expression outside the loop.
                    popped_item = numbers_stack.pop()
                    result.append(popped_item)

            # reverting and joining items from array to be used in eval()
            a = result[::-1]
            calc = "".join(a)
            print(f'Calc: {calc}')

            # using eval() to get the calculation and pushing it back to stack with str()
            eval_calc = eval(calc)
            numbers_stack.push(str(eval_calc))
            result.clear()

    return numbers_stack.peek()


# TEST!
print(f'Returning: {eval_postfix(expression)}')
print(f'Expression: {expression}, Answer: {answer}')


