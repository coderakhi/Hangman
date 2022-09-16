# HANGMAN

import random
from hangman_words import word_list
from hangman_art import stages

# random.choice select a random element from a list
chosen_word=random.choice(word_list)
print(chosen_word)

lives=6 #there are 6 lives initially

# this block of code creates ['_','_'...] based on the length of the word chosen.
display=[]
word_length=len(chosen_word)
for i in range(word_length):
    display.append("_")


end_of_game=False #create a flag so the while loop runs till it becomes true
while not end_of_game:
    guess = input("Guess a letter: ").lower() # we need to create a user input function to guess the letter
    for letter in enumerate(chosen_word): #enumerate outputs tuple where one value is the index and the element
        # Check guessed letter
        if letter[1]==guess:
            display[letter[0]]=letter[1] #reassigning "_" to the letter
    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost")
    # Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game=True
        print("Youn win")

    print(stages[lives])











