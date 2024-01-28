import random
from brain_games.runner import run_game
from brain_games.constants import PRIME_INSTRUCT
from brain_games.constants import MIN_NUMBER, MAX_NUMBER


def is_prime(number):
    for divisor in range(MIN_NUMBER, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def get_num_and_prime_ans():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(number) else 'no'

    return number, answer


def run_prime_game():
    run_game(get_num_and_prime_ans, PRIME_INSTRUCT)
