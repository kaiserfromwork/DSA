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

math_symbols = ['+', '-', '*', '/']
numbers_stack = Stack()
expression, answer = postfix_expressions[random.randint(0, len(postfix_expressions) - 1)]


def eval_postfix(math_expression):
    result = []
    for char in math_expression:
        if char not in math_symbols:
            # print(f'{char} pushed to Stack')
            numbers_stack.push(char)
        else:
            counter = 0
            # print(f'{char} is a math symbol')
            print(numbers_stack.pop())
            while counter < 2:
                if numbers_stack.is_empty():
                    break
                if numbers_stack.peek() == " ":
                    counter += 1
                    if counter < 2:
                        result.append(char)
                        # print(f"Added symbol to expression: {char}")
                        numbers_stack.pop()
                else:
                    popped_item = numbers_stack.pop()
                    result.append(popped_item)
                    print(f"Added number to expression: {popped_item}")

            # print(f'Value of result: {result}')
            a = result[::-1]
            calc = "".join(a)
            print(f'Calc: {calc}')
            eval_calc = eval(calc)
            # print(f'eval calc: {eval_calc}')
            numbers_stack.push(str(eval_calc))
            result.clear()

    return numbers_stack.peek()


print(f'Returning: {eval_postfix(expression)}')
print(f'Expression: {expression}, Answer: {answer}')


