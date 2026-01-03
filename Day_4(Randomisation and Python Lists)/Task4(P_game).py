import random

print("Rock, paper, scissor Game")

rock = ''' 
    -------
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)


'''
scissor = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)


'''

game_image = [rock, paper, scissor]


user_choice = int(input("what do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors  "))

if user_choice >=0 and user_choice <=2:
    print(game_image[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_image[computer_choice])

# 0, 1, 2

computer_choice = random.randint(0,2)
print(f"Computer choose {computer_choice}")

if user_choice >=3 or user_choice < 0:
    print("you typed a invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice ==2:
    print("Computer Win!")
elif computer_choice > user_choice:
    print("Computer Win!")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice == user_choice:
    print("It's a draw!")
