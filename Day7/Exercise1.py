##      Challenge 1- Picking a random Words and Checking

world_list = ["aardvark", "baboon", "camel"]

# TODO -1 => Randomly choose a word from the word_list and assign it ti a variable called chosen_word.

import random

chosen_word = random.choice(world_list)

# TODO -2 => Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercases.

guess = input("Guess a letter: ").lower()


# TODO -3 => Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
