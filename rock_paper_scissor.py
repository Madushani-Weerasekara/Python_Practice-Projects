import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit. ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2) # rock:0, paper:1, scissors:2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    # Check for a tie first
    if user_input == computer_pick:
        print("Nobody won this time!")
    
    # Check if the user won
    elif user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
  
     # If it's not a tie or win, the user lost
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
    