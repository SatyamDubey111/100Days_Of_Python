import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# probably should check whether the inputs are valid, but since they were part of the assignment...
# made them a little more readable though
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbol would you like?\n"))
nr_numbers = int(input("how many number would you like?\n"))

# Easy Level
# password = ""
# 0, 1, 2, 3 range(0, 4)
# nr_letters = 4
# for char in range(1, nr_letters + 1):  + 1 removed from all working same
# for char in range(0, nr_letters):
    # 1 - 4
    # random_char = random.choice(letters)
    # print(random_char)
    # password += random.choice(letters)
    # print(password)
# for char in range(0, nr_symbols ):
    # password += random.choice(symbols)

# for char in range(0, nr_numbers):
    # password += random.choice(numbers)

# print(password)


# HARD LEVEL

password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
