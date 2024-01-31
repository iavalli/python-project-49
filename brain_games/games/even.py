import random


def is_number_even(number):
    """checks whethet the number is even"""
    return number % 2 == 0


def get_num_and_correct_ans() -> tuple:
    """returns a random number and the correct answer"""
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_number_even(number) else 'no'
    return number, correct_answer
