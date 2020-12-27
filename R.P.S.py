import random

def gameOn():
  choice = ["rock", "paper", "scissors"]

  computer_choice = random.choice(choice)
  player_choice = input("Please chose Rock/Paper/Scissors: ")
  player_choice = player_choice.lower()

  while True:
    if computer_choice == player_choice:
      print("You chose the same.")

    elif computer_choice == "rock" and player_choice == "paper":
      print("You win! Paper beats Rock.")
    elif computer_choice == "rock" and player_choice == "scissors":
      print("You lose! Rock beats Scissors.")

    elif computer_choice == "paper" and player_choice == "rock":
      print("You lose! Paper beats Rock.")
    elif computer_choice == "paper" and player_choice == "scissors":
      print("You win! Scissors beats Paper.")

    elif computer_choice == "scissors" and player_choice == "rock":
      print("You win! Rock beats Scissors.")
    elif computer_choice == "scissors" and player_choice == "paper":
      print("You lose! Scissors beats Paper.")

    answer = input("Would you like to play again? Yes/No ")
    if answer in ("yes", "Yes", "y", "Y", "yup"):
      print("Game starting again!")
      gameOn() 
    else:
      print("Goodbye!")
    break

gameOn()
