import random
from brain_games.runner import run_game
from brain_games.constants import PROGRESSION_INSTRUCTION, MIN_PROGR_LENGTH
from brain_games.constants import MAX_PROGR_LENGTH


def get_progression_and_answer():
    start, step = random.randint(1, 100), random.randint(1, 100)
    progr_length = random.randint(MIN_PROGR_LENGTH, MAX_PROGR_LENGTH)
    missed_index = random.randint(0, progr_length - 1)

    progression = []
    for i in range(progr_length):
        progression.append(start + step * i)

    missed_index = random.randint(0, progr_length - 1)
    missed_num = progression[missed_index]
    progression[missed_index] = '..'
    progression_with_missed_num = ' '.join(map(str, progression))

    return progression_with_missed_num, str(missed_num)


def run_progression_game():
    run_game(get_progression_and_answer, PROGRESSION_INSTRUCTION)
