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


def print_option(action):
    if action == 0:
        return rock
    elif action == 1:
        return paper
    else:
        return scissor


def check_result(user_sel_action, computer_sel_action):
    if user_sel_action == computer_sel_action:
        print(f'Both Players selected {print_option(user_sel_action)}. It\'s a tie!')
    elif user_sel_action == 0:
        if computer_sel_action == 2:
            print('Rock smashes scissors You win!')
        else:
            print("Paper covers You lose.")
    elif user_sel_action == 1:
        if computer_sel_action == 0:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_sel_action == 2:
        if computer_sel_action == 1:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


continue_playing = 'Y'
while continue_playing.upper() == 'Y':
    user_action = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
    if user_action not in (0, 1, 2):
        print('Invalid Input, Please Type 0 for Rock, 1 for Paper or 2 for Scissors.')
        pass
    computer_action = random.randint(0, 2)
    print('You chose:')
    print(f'{print_option(user_action)}')
    print('Computer chose:')
    print(f'{print_option(computer_action)}')
    check_result(user_action, computer_action)
    continue_playing = input('Do you want to Play again? Type Y or N -> ')
    if continue_playing.upper() not in ('Y', 'N'):
        print('Invalid replay Input')
        break
