import random

word_list = ["aardvark", "baboon", "Camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
word_length = len(chosen_word)
# for position in range(1, 6):
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - use a while loop to let the user guess again

game_over = False

correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

# TODO-2: change the for loop so thqt you keep the previous correct

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" in display:
        game_over = True
        print("You win.")
