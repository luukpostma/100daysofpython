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

game_art = [rock, paper, scissors]

# player becomes 0, 1 or 2
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)

# print(game_art[computer])
print(f"You choose: {game_art[player]}")
print(f"Computer choose: {game_art[computer]}")

# game logic
if player < 0 or player > 2:
    print("Invalid choice. You lose!")
elif (player == 0 and computer == 1 or
      player == 1 and computer == 2 or
      player == 2 and computer == 0):
    print("You lose!")
elif (player == 0 and computer == 2 or
      player == 1 and computer == 0 or
      player == 2 and computer == 1):
    print("You win!")
