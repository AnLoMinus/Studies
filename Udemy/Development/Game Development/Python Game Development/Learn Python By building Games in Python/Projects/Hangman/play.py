

# 1. Import the wanted Python module.
import random

# 2. Pick and save the words to be guessed as a list in Hangman_guessing.py file. Note: (all the words to be guessed consist of six letters)
from hangman_guessing import guess_list

# 3. Use the imported Python module to pick a random word from the words you save.
guessing_word = random.choice(guess_list).lower()
word_letters = len(guessing_word)

# 4. keep the game runnig until the game is over.
game_over = False

# 5. Apply tries to the players to use to try to win.
tries = 6

# 6. Save game shapes in hangman_life.py file and import those shapes from this file.
from hangman_life import game_name
print(game_name)

# 7. Test the code you wrriten until now using Python print function.
print(f'The word you guessed is {guessing_word}')

# 8. create a list contains six '. underscore to store and save the right letter guessed by the players of the random word.
result = []

# 9. Iterate over the players input.
abcd = '_'
for abcd in range(word_letters):
    result += '_'

# 10. Inform the players about the letter they have guessed after they do.
while not game_over:
    user_guessing = input("Guess a letter: ")

# 11. Check if the guessed letters by the players is right or wrong.
    if user_guessing in result:
        print(f'The letter you have guessed is {user_guessing}')

# 12. The players lose a try if they guessed wrong letter.
    for position in range(word_letters):
        letter = guessing_word[position]
        if letter == user_guessing:
            result[position] = letter

# 13. If the players lose all their tries end game and print the end game message.
    if user_guessing not in guessing_word:
        print(f'You guessed {user_guessing}, This letter is not in the word, you lose a try')

# 14. Join all the letters which in the list of guessed letter and turn it into string.
        tries -= 1
        if tries == 0:
            game_over = True
            print(' Game Over, You Lose the Game, try again later.. ')

# 15. Check if the player guessed all the right letter so end game and print the win message.
    print(f"{' '.join(result)}")

# 16. You to print the correct shape after every players try.
    if '_' not in result:
        game_over = True
        print('You are a winner, Congratulations')

# 17. Print the correct shape after every players try.
from hangman_life import lives
print(lives[tries])
