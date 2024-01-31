#!/usr/bin/env python3
from brain_games.constants import GCD_INSTRUCTION
from brain_games.games.gcd import get_numbers_and_answer
from brain_games.runner import run_game


def main():
    run_gcd_game()


def run_gcd_game():
    run_game(get_numbers_and_answer, GCD_INSTRUCTION)


if __name__ == '__main__':
    main()
