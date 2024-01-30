#!/usr/bin/env python3
from brain_games.constants import CALC_INSTRUCTION
from brain_games.runner import run_game
from brain_games.games.calc import get_expression_and_result


def main():
    run_calc_game()


def run_calc_game():
    run_game(get_expression_and_result, CALC_INSTRUCTION)


if __name__ == '__main__':
    main()
