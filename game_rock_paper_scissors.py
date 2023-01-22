import random
import colorama
from colorama import Fore

# user input
player_move = input("Choose [r]ock, [p]aper or [s]cissoer: ")

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

# logic

# 1.Possible choices of the player
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

# 2.Possible choices of the computer
computer_move = ""

computer_random_number = random.randint(1, 3)
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

print(f"The computer chose {computer_move}.")

# output - winner check
if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print(Fore.GREEN + "You win!")
elif player_move == computer_move:
    print(Fore.YELLOW + "Draw!")
else:
    print(Fore.RED + "You lose!")

