# software development method. 
# First the program wil greet the player
# Then the player is given a choice to choose rock, paper or scissors.
# If the player doesn't follow the rules they'll be bet by a surprise.
# Then the computer player randomly chooses their move, and then we determine who won and display a "You won!", "You lost!" or "Draw" message
import random 
print("Welcome to the Rock, Paper, Scissors game!")
print("Please type 1, 2, or 3 and then press Enter to select either Rock, Paper or Scissors respectively.\n\tChoose wisely")
player_choice = input()
if(not player_choice.isdigit()):
    print("The AI choses a katana.\n\tYou Lose!")
    exit()
if (int(player_choice) > 3 or int(player_choice) < 1):
    print("The AI choses a katana.\n\tYou Lose!.")
    exit()
player_choice = int(player_choice)
#we could check if the number is a valid number or we could generate the computer player's move choice here too.
ai_choice = random.randint(1, 3)
moves_dict = {1:"Rock", 2:"Paper", 3:"Scissors"}
ai_choice_string = moves_dict[ai_choice] #looks up the associated string in the moves dictionary by using the dictionar[a key value]
player_choice_string = moves_dict[player_choice]
print(f"The AI chose {ai_choice_string}")
print(f"You chose {player_choice_string}")
#1 is rock 2 is paper 3 is rock
if ((player_choice == 1 and ai_choice == 3) or (player_choice == 2 and ai_choice == 1) or (player_choice == 3 and ai_choice == 2)):
    print("You won!")
elif ((player_choice == 1 and ai_choice == 1) or (player_choice == 2 and ai_choice == 2) or (player_choice == 3 and ai_choice == 3)):
    print("Draw!")
else:
    print("You lose!")