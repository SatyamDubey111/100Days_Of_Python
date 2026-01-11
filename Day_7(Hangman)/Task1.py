import random

word_list = ["aardvark", "baboon", "Camel"]

#TODO-1 - Randomly choose a word from the word _list and asign it to,
# a  variable called choosen_word.then print it .
# import random  -> import should be at very top of the list

chosen_word = random.choice(word_list)
print(chosen_word)

# 2

placeholder = ""
word_length = len(chosen_word)
# for position in range(1, 6):
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-2 - Ask the user to guess a letter and asign their answer to a variable called guess,
# MAke guess lower case
guess = input("Guess a letter: ").lower()
print(guess)

# 2




# TODO -3 CHeck if the letter the user guessed (guess) is one of the letters in the choosen word print "right",
#  if it is "wrong" if it's not.

