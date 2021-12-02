import random
from hangman_art import logo, HANGMANPICS
from replit import clear

# Open the file in read mode
with open("list.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split(",")))

# random word chosen
chosen_word = random.choice(words)
# print(chosen_word)
print(logo)

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
print(display)


def getGuess(alreadyGuessed):
    '''
    Returns the letter the player entered. This function makes sure the player
    entered a single letter and not something else
    '''
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print(f"You've have already guessed the letter {guess} Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER")
        else:
            return guess.lower()


end_of_game = False
lives = 0
missedLetters = ''
correctLetters = ''
while not end_of_game:
    guess = getGuess(correctLetters + missedLetters)
    clear()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter.lower() == guess:
            display[position] = letter
            correctLetters += guess
    print(display)
    if guess not in chosen_word.lower():
        missedLetters += guess
        print(f"You guessed {guess}, that's not in the word. You loose a life.")
        print(HANGMANPICS[lives])
        lives += 1
        if lives == 7:
            print('You loose!')
            end_of_game = True

    if "_" not in display:
        end_of_game = True
        print("You win!")
