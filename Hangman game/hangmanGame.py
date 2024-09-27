import random
from Hangman_words import word_list
from Hangman_art import logo, stages


print(logo)
print("\n\nWelcome to Hangman!\n")
print("Guess a letter to start. If you guess a letter correctly, it will be revealed in the word.")
print("If you guess incorrectly, you will lose a life. The game will end when you guess the word or run out of lives.")

# Initialize game variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ['_'] * word_length
guessed_letters = []
lives = 6
game_over = False

while not game_over:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print(f"\nYou already guessed {guess}. Try again!\n")
        continue

    guessed_letters.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Print the updated display
    print(' '.join(display))

    # Check if the guess is not in the word
    if guess not in chosen_word:
        print(f"\n\nIncorrect! You lose a life. You have {lives - 1} lives left.")
        lives -= 1

    # Check if the game is over
    if lives == 0:
        game_over = True
        print("\nYou lost! The word was-  " + chosen_word)
    elif '_' not in display:
        game_over = True
        print("\nYou won! Congratulations!")

    # Print the hangman stage
    print(stages[lives])