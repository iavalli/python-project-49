import random
from brain_games.constants import MATH_ACTIONS


def make_action(num1, num2, math_action):
    """generates an operation depending on the math action"""
    if math_action == '+':
        return num1 + num2
    elif math_action == '-':
        return num1 - num2
    elif math_action == '*':
        return num1 * num2


def get_expression_and_result():
    """generates an expression with two random numbers and the correct answer"""
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_action = random.choice(MATH_ACTIONS)

    result = make_action(num1, num2, math_action)
    expression = f'{num1} {math_action} {num2}'

    return expression, str(result)
