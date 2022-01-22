import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_number(guessed_number, input_number):
    if input_number > guessed_number:
        print('Too high.')
    elif input_number < guessed_number:
        print('Too low.')
    else:
        print(f'You got it! The answer was {input_number}')


def guess_number():
    guessed_number = random.randint(1, 100)
    print(logo)
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard' : ")

    if 'easy' == difficulty_level:
        print('You have 10 attempts remaining to guess the number.')
        input_count = EASY_LEVEL_TURNS
    elif 'hard' == difficulty_level:
        print('You have 5 attempts remaining to guess the number.')
        input_count = HARD_LEVEL_TURNS
    else:
        print('Invalid input')
        exit(0)

    while input_count > 0:
        input_number = int(input('Make a guess: '))
        input_count -= 1
        check_number(guessed_number, input_number)
        if input_number == guessed_number:
            exit(0)
        if input_count > 0:
            print('Guess again')
            print(f'You have {input_count} attempts remaining to guess the number')


guess_number()
