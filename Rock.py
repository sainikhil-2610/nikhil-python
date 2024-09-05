import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Enter rock, paper, or scissors: ")
if player == computer:
    print("Tie!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("Player wins!")
else:
    print("Computer wins!")
