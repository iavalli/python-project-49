import prompt
import random


def welcome_user():
    print('brain-even\n')
    print('Welcome to the Brain Games!\n')
    global name
    name = prompt.string('May I have your name? ')
    print(f'\nHello, {name}!')
    print('\nAnswer "yes" if the number is even, otherwise answer "no".\n')
    return name


def put_question_get_answer():
    global number
    number = random.randint(1, 100)
    print(f'Question: {number}')
    global answer
    answer = prompt.string('Your answer: ')
    return number, answer


def correct_answer():
    global i
    i = 0
    print('Correct!')
    i += 1
    put_question_get_answer()
    if i == 3:
        print('Congratulations!\n')
    return


def check_answer(number, answer, name):
    if (number % 2 == 0 and answer == 'yes'):
        correct_answer()
    elif (number % 2 != 0 and answer == 'no'):
        correct_answer()
    elif (number % 2 == 0 and answer == 'no'):
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
        print(f"Let's try again, {name}!")
        return
    elif (number % 2 != 0 and answer == 'yes'):
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
        print(f"Let's try again, {name}!")
        return
    else:
        return


welcome_user()
put_question_get_answer()
check_answer(number, answer, name)
