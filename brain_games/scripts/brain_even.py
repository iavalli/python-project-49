#!/usr/bin/env python3
from brain_games.runner import run_game
from brain_games.constants import EVEN_INSTRUCTION
from brain_games.games.even import get_num_and_correct_ans


def main():
    run_even_game()


def run_even_game():
    run_game(get_num_and_correct_ans, EVEN_INSTRUCTION)


if __name__ == '__main__':
    main()
