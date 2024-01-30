import random
from brain_games.constants import MATH_ACTIONS


def get_expression_and_result():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_action = random.choice(MATH_ACTIONS)
    expression = f'{num1} {math_action} {num2}'
    result = eval(expression)

    return expression, str(result)
