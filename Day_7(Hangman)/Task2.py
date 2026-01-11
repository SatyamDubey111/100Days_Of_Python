import random

word_list = ["aardvark", "baboon", "Camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# Todo-1: create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)
# for position in range(1, 6):
for position in range(word_length):
    placeholder += "_"
print(placeholder)


guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts thw guess in the right position

# for letter in chosen_word:
#     if letter == guess:
#        print("right")
#     else:
#         print("wrong")


display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)