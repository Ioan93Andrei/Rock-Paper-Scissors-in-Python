import random
import messages

def gameOn():
  choice = ["rock", "paper", "scissors"]

  computer_choice = random.choice(choice)
  player_choice = input("Please chose Rock/Paper/Scissors: ")
  player_choice = player_choice.lower()

  while True:

    #Makes sure the user enters a valid option.
    if player_choice not in("rock", "paper", "scissors"):
      print("Choice is not correct!")

    #Prints in case both the computer and the player chose the same option.
    elif computer_choice == player_choice:
      print("You chose the same.")

    #Computer choses ROCK.
    elif computer_choice == "rock" and player_choice == "paper":
      print(messages.against_rock_win)
    elif computer_choice == "rock" and player_choice == "scissors":
      print(messages.against_rock_lose)

    #Computer choses PAPER.
    elif computer_choice == "paper" and player_choice == "rock":
      print(messages.against_paper_lose)
    elif computer_choice == "paper" and player_choice == "scissors":
      print(messages.against_paper_win)
      
    #Computer choses SCISSORS.
    elif computer_choice == "scissors" and player_choice == "rock":
      print(messages.against_scissors_win)
    elif computer_choice == "scissors" and player_choice == "paper":
      print(messages.against_scissors_lose)
      
    #Asks the user if he/she wants to play again and restarts the loop if so.
    answer = input("Would you like to play again? Yes/No ")
    if answer in ("yes", "Yes", "y", "Y", "yup"):
      print("Game starting again!")
      gameOn() 
    else:
      print("Goodbye!")
    break

gameOn()
