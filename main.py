import random
import messages

def gameOn():
  choice = ["rock", "paper", "scissors"]
  total_score = 0

  while True:
    computer_choice = random.choice(choice)
    player_choice = input("Please chose Rock/Paper/Scissors: ")
    player_choice = player_choice.lower()

    while True:
      #Makes sure the user enters a valid option.
      if player_choice not in("rock", "paper", "scissors"):
        print("Choice is not correct!")
        break

      #Prints in case both the computer and the player chose the same option.
      elif computer_choice == player_choice:
        print("You chose the same.")
      
      #Computer choses ROCK.
      elif computer_choice == "rock" and player_choice == "paper":
        print(messages.win[0])
        total_score += 1
        print(total_score)
      elif computer_choice == "rock" and player_choice == "scissors":
        print(messages.lose[0])
        total_score -= 1
        print(total_score)

      #Computer choses PAPER.
      elif computer_choice == "paper" and player_choice == "rock":
        print(messages.lose[1])
        total_score -= 1
        print(total_score)
      elif computer_choice == "paper" and player_choice == "scissors":
        print(messages.win[1])
        total_score += 1
        print(total_score)

      #Computer choses SCISSORS.
      elif computer_choice == "scissors" and player_choice == "rock":
        print(messages.win[2])
        total_score += 1
        print(total_score)
      elif computer_choice == "scissors" and player_choice == "paper":
        print(messages.lose[2])
        total_score -= 1
        print(total_score)
        
      #Asks the user if he/she wants to play again and restarts the loop if so.
      answer = input("Would you like to play again or see your score? Yes/No/Score ")
      if answer in ("Score", "score"):
        print("Your total score is " + str(total_score)) 
        answer = input("Would you like to play again or see your score? Yes/No/Score ")
        print("Game starting again!")
      elif answer in ("yes", "Yes", "y", "Y", "yup"):
        print("Game starting again!")
      else:
        print("Goodbye!")
      break

gameOn()