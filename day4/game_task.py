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
import random
import sys
game = [rock, paper, scissors]
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if player_input >2:
    print("Choose a correct choice!")
    sys.exit()

player = game[player_input]
computer = random.choice(game)
print(player)
print("computer chose:")
print(computer)

if player == computer:
    print("It's a tie!")
elif player == rock and computer == scissors:
    print("You win!")
elif player == rock and computer == paper:
    print("You lose!")
elif player == scissors and computer == paper:
    print("You win!")
elif player == scissors and computer == rock:
    print("You lose!")
elif player == paper and computer == rock:
    print("You win!")
elif player == paper and computer == scissors:
    print("You lose!")
else:
    print("Choose a correct choice!")
