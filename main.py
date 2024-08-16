import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

lives = 6

print(logo)
chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ''
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += '_'
print('Word to guess: ' + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # Tell the user how many lives they have left.
    print(f'****************************{lives}/6 LIVES LEFT****************************')
    guess = input('Guess a letter: ').lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f'You have already guessed "{guess}"!')

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print('Word to guess: ' + display)

    # If the letter is not in the chosen_word, print out the letter and let user know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        print(f'You guessed "{guess}", that is not in the word. You lose a life!')
        lives -= 1

        if lives == 0:
            game_over = True

            # Show the correct word to user.
            print(f"***********************Correct word is '{chosen_word}'. YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
