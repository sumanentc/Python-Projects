import random
import sys

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
if nr_letters > 52:
    sys.exit('Number of letters should be less than 52')
nr_symbols = int(input(f"How many symbols would you like?\n"))
if nr_symbols > 9:
    sys.exit('Number of symbols should be less than 9')
nr_numbers = int(input(f"How many numbers would you like?\n"))
if nr_numbers > 10:
    sys.exit('Number should be less than 10')

symbol_dict = {0: letters, 1: symbols, 2: numbers}
symbol_count_dict = {0: nr_letters, 1: nr_symbols, 2: nr_numbers}
positions = list(range(0, 3))
random.shuffle(positions)
generated_password = ''
for p in positions:
    selected_list = symbol_dict[p]
    chosen_characters = random.sample(range(len(selected_list)), symbol_count_dict[p])
    for s in chosen_characters:
        generated_password += selected_list[s]
print('Here is your secure Password!!')
print(generated_password)
