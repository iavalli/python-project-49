import math
import random

from brain_games.runner import run_game
from brain_games.constants import GCD_INSTRUCTION


def get_numbers_and_answer():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    numbers = f'{num1} {num2}'
    gcd = math.gcd(num1, num2)

    return numbers, str(gcd)


def run_gcd_game():
    run_game(get_numbers_and_answer, GCD_INSTRUCTION)
