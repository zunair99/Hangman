import random
import words
from words import words
print (words)
import string

def valid_words(words):
    word = random.choice(words)
    while  "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = valid_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()


    lives = 6

    while len(word_letters) >0 and lives > 0:
        print ("You have", lives, "lives left and you have used these letters: ", "".join(used_letters)) 

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print ("Current word: ", "".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print ("Letter is not in the word.")
        elif user_letter in used_letters:
            print ("You have already used that letter. Please try again.")
        else:
            print ("Invalid character. Please try again.")

    if lives == 0:
        print("Sorry, you're out of lives. The word was", word)
    else:
        print("You guessed the word", word, "!")
        
hangman()

user_input = input("Type something: ")
print(user_input)
