#!/usr/bin/env python3
from brain_games.runner import run_game
from brain_games.constants import PRIME_INSTRUCT
from brain_games.games.prime import get_num_and_prime_ans


def main():
    run_prime_game()


def run_prime_game():
    run_game(get_num_and_prime_ans, PRIME_INSTRUCT)


if __name__ == '__main__':
    main()
