import random

total_palyed = 0
user_wins = 0
computer_wins = 0
draw = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    total_palyed += 1
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if((user_input == "rock" and computer_pick == "rock") or (user_input == "scissors" and computer_pick == "scissors")
                    or (user_input == "paper" and computer_pick == "paper")):
        print("Nobody wins! it's a draw")
        draw += 1
        
    elif user_input == "rock" and computer_pick == "scissors":
        print("You won")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("Total played", total_palyed, "times")
print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print("Draw:", draw)
print("Goodbye")


