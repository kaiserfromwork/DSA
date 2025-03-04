# Problem
# Balanced Parentheses – Check if
# a given expression has balanced parentheses {}, [], ()


from data_structures.stack import Stack
import random

expressions = [
    ("([])", "Balanced"),
    ("({[]})", "Balanced"),
    ("([)]", "Unbalanced: mismatched order"),
    ("(((", "Unbalanced: missing closing parentheses"),
    ("[]", "Balanced"),
    ("{[()]}", "Balanced"),
    ("{", "Unbalanced: missing closing brace"),
    ("}", "Unbalanced: missing opening brace"),
    ("([{}])", "Balanced"),
    ("([{}]", "Unbalanced: missing closing parenthesis"),
    ("([]", "Unbalanced: missing closing bracket"),
    ("())", "Unbalanced: extra closing parenthesis"),
    ("(([]){})", "Balanced"),
    ("[{()}]", "Balanced"),
    ("(([]){})}", "Unbalanced: extra closing brace"),
    ("({[)]", "Unbalanced: wrong closing order"),
    ("", "Balanced: empty string (nothing to check)"),
    ("({})[", "Unbalanced: missing closing bracket"),
    ("(([]){})(", "Unbalanced: missing closing parenthesis")
]

s = Stack()

random = random.randint(0, len(expressions) - 1)
check_expression = expressions[random][0]
check_expression_result = expressions[random][1]

valid_input = {')': '(', ']': '[', '}': '{'}

if check_expression == "":
    print("Expression is empty!")
    print(check_expression_result)
else:
    for char in check_expression:
        if char in valid_input.values():
            s.push(char)
        elif char in valid_input:
            if not s.is_empty() and s.peek() == valid_input[char]:
                s.pop()
    if s.is_empty():
        print(f'{check_expression} is valid!')
        print(f'{check_expression} is {check_expression_result}!')

    else:
        print(f'{check_expression} is not valid!')
        print(f'{check_expression} is {check_expression_result}!')
