import random
from brain_games.constants import MATH_ACTIONS, CALC_INSTRUCTION
from brain_games.runner import run_game


def get_expression_and_result():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_action = random.choice(MATH_ACTIONS)
    expression = f'{num1} {math_action} {num2}'
    result = eval(expression)

    return expression, str(result)


def run_calc_game():
    run_game(get_expression_and_result, CALC_INSTRUCTION)
