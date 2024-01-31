#!/usr/bin/env python3
from brain_games.runner import run_game
from brain_games.games.progression import get_progression_and_answer
from brain_games.constants import PROGRESSION_INSTRUCTION


def main():
    run_progression_game()


def run_progression_game():
    run_game(get_progression_and_answer, PROGRESSION_INSTRUCTION)


if __name__ == '__main__':
    main()
