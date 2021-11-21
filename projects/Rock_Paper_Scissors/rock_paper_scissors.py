# To check the rules of rock paper scissors game follow https://wrpsa.com/the-official-rules-of-rock-paper-scissors/
import random

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print('Welcome to the Rock Paper Scissors Game!')
print(f'Rock -> {rock}')
print(f'Paper -> {paper}')
print(f'Scissor -> {scissor}')
print('----------------------------------------')

ROCK_ACTION = 0
PAPER_ACTION = 1
SCISSORS_ACTION = 2


def print_option(action):
    if action == ROCK_ACTION:
        return rock
    elif action == PAPER_ACTION:
        return paper
    else:
        return scissor


def check_result(user_sel_action, computer_sel_action):
    if user_sel_action == computer_sel_action:
        print(f'Both Players selected {print_option(user_sel_action)}. It\'s a tie!')
    elif user_sel_action == ROCK_ACTION:
        if computer_sel_action == SCISSORS_ACTION:
            print('Rock smashes scissors You win!')
        else:
            print("Paper covers You lose.")
    elif user_sel_action == PAPER_ACTION:
        if computer_sel_action == ROCK_ACTION:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_sel_action == SCISSORS_ACTION:
        if computer_sel_action == PAPER_ACTION:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


continue_playing = 'Y'
invalid_input = False
while continue_playing.upper() == 'Y':
    try:
        user_action = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. -> '))
    except ValueError:
        print('Invalid Input!')
        continue
    if user_action not in (0, 1, 2):
        print('Invalid Input!')
        invalid_input = True
    if invalid_input:
        continue
    else:
        computer_action = random.randint(0, 2)
        print('You chose:')
        print(f'{print_option(int(user_action))}')
        print('Computer chose:')
        print(f'{print_option(computer_action)}')
        check_result(int(user_action), computer_action)
        continue_playing = input('Do you want to Play again? Type Y or N -> ')
        if continue_playing.upper() not in ('Y', 'N'):
            print('Invalid replay Input, Closing the game')
            break
