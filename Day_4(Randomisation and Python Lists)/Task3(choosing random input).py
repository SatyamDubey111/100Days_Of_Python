import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Option
print(random.choice(friends))  # choice is  a function

# 2nd Option
random_index = random.randint(0,4)
print(friends[random_index])

#  when we working with list often we have to face with , indexError: index out of range

# print(friends[50])  # list out of range

fruits = ["strawberries", "Netarines", "Apples", "Grapes", "peaches"]
vegetable =["Spinah", "Kale", "Tamatoes", "gajar"]

dirty_dozen =[fruits, vegetable]
print(dirty_dozen)