
# rock paper scissor game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input(
    "What do you want to print? Type 0 for rock, Type 1 for paper, Type 2 for scissors/n: "))

print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("compute choice:")

print(game_images[computer_choice])

if (user_choice >= 3) or (user_choice < 0):
    print("You typed invalid input, You loose")
elif user_choice == 0 and computer_choice == 1:  # rock - paper - win
    print("You Win")
elif user_choice == 1 and computer_choice == 2:  # paper - scissor - win
    print("You Win")
elif user_choice == 2 and computer_choice == 0:  # scissor - rock - loose
    print("You Loose")
elif computer_choice > user_choice:
    print("Its a loose")
elif computer_choice < user_choice:
    print("Its a Win")
elif computer_choice == user_choice:
    print("Its a Draw")
