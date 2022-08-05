import random

print("Welcome to ROCK/PAPER/SCISSORS game!")
computer_wins = 0
user_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    choice = input("Enter a choice(rock/paper/scissors) or q to quit :").lower()
    if choice == "q":
        break
    if choice not in options:
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if choice == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif choice == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif choice == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye!!!")
