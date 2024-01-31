import random
from brain_games.constants import MIN_PROGR_LENGTH, MAX_PROGR_LENGTH


def generate_progression():
    """generates a progression and a missed index"""
    start, step = random.randint(1, 100), random.randint(1, 100)
    progr_length = random.randint(MIN_PROGR_LENGTH, MAX_PROGR_LENGTH)
    missed_index = random.randint(0, progr_length - 1)

    progression = []
    for i in range(progr_length):
        progression.append(start + step * i)

    return progression, missed_index


def get_progression_and_answer():
    """returns a progression with a missed number and the correct answer"""
    progression, missed_index = generate_progression()

    missed_num = progression[missed_index]
    progression[missed_index] = '..'
    progression_with_missed_num = ' '.join(map(str, progression))

    return progression_with_missed_num, str(missed_num)
