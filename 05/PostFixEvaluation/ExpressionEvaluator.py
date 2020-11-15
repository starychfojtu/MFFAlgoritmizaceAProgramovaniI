import Stack as s

OPERATORS = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a // b)
}

def evaluate_postfix(expression):
    """
    Evaluates postfix expression in string. Throws exception if expression is invalid or cannot be evaluated (e.g division by zero).
    """

    parts = expression.split()
    stack = s.Stack()
    for part in parts:
        if part in OPERATORS.keys():
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = OPERATORS[part](arg2, arg1)
            stack.push(result)
        else:
            stack.push(int(part))

    result = stack.pop()
    
    assert stack.count() == 0

    return result