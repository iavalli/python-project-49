import random
from brain_games.constants import MIN_NUMBER, MAX_NUMBER


def is_prime(number):
    """checks if the given number is a prime one"""
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def get_num_and_prime_ans():
    """returns the number and the correct answer"""
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = 'yes' if is_prime(number) else 'no'

    return number, answer
