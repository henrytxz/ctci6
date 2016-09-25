"""
16.26 Calculator
Given an arithmetic equation, +ve ints, +,-,* and /
for eg,
input: "2*3+5/6*3+15"
output: 23.5

thoughts:
perhaps take in the str, break it by the operators
break by + and - 1st?
2*3, 5/6*3, 15
"""

import re

def calculate(expr):
    sub_expressions = re.split('[+-]', expr)
    sub_expr_values = []
    for sub_expr in sub_expressions:
        sub_expr_values.append(multiply_divide(sub_expr))
    if not sub_expressions:
        return 0
    plus_and_minus = []
    for c in expr:
        if c == '+' or c == '-':
            plus_and_minus.append(c)
    i = 0
    result = sub_expr_values[i]
    for op in plus_and_minus:   # +
        i += 1
        if op == '+':
            result += sub_expr_values[i]    # result = 8.5 + 15 = 23.5
        else:
            result -= sub_expr_values[i]
    return result

def multiply_divide(expr):  # 2*3   when working on this problem, I'm practicing for technical phone interviews so I'm using comments while I run thru a test case
    """
    for 5/6*3, / is at 1 and * is at 3
    for 15
    """
    operators = []
    operator_positions = []
    for i, c in enumerate(expr):
        if c == '*' or c == '/':
            operators.append(c) # *
            operator_positions.append(i)    # 0

    if operator_positions:
        last_operator_pos = operator_positions.pop(0)   # 0
    else:
        last_operator_pos = len(expr)  # 2

    try:
        result = float(expr[:last_operator_pos])  # expr[:2] => 15
    except ValueError, e:
        raise ValueError('an invalid expression: {0} was passed in'.format(expr))
    for operator in operators:  # *
        if operator_positions:
            next_operator_pos = operator_positions.pop(0)
        else:
            next_operator_pos = len(expr)   # 3
        try:
            if operator == '*':
                result *= float(expr[last_operator_pos+1 : next_operator_pos])    # expr[2:3] => 3, result = 6
            else:
                result /= float(expr[last_operator_pos+1 : next_operator_pos])
        except ValueError, e:
            raise ValueError('an invalid expression: {0} was passed in'.format(expr))
        last_operator_pos = next_operator_pos   # 3
    return result   # 6

if __name__ == '__main__':
    assert calculate("2*3+5/6*3+15") == 23.5
    assert calculate('8*9/3') == 24

