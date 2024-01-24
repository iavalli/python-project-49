import random
from brain_games.runner import run_game
from brain_games.constants import EVEN_INSTRUCTION


def is_number_even(number):
    return number % 2 == 0


def get_num_and_correct_ans() -> tuple:
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_number_even(number) else 'no'
    return number, correct_answer


def run_even_game():
    run_game(get_num_and_correct_ans, EVEN_INSTRUCTION)
