import prompt
from brain_games.constants import ROUNDS_NUMBER
from brain_games.constants import EVEN_INSTRUCTION

instruction = EVEN_INSTRUCTION


def run_game(get_num_and_correct_ans, instruction):
    print('Welcome to the Brain Games!\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{instruction}')

    for _ in range(ROUNDS_NUMBER):
        question, correct_answer = get_num_and_correct_ans()
        user_answer = prompt.string(f'Question: {question}\n'
                                    f'Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
