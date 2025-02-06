# Rock, Paper, Scissors Game with Simple Score Tracking.

import random

# Options for the game
choices = ["rock", "paper", "scissors"]

# Initialize scores
player_score = 0
computer_score = 0

while True:
    # Player choice
    player_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()

    # Exit condition
    if player_choice == "exit":
        print(f"Final Scores -> Player: {player_score}, Computer: {computer_score}")
        break

    # Validate input
    if player_choice not in choices:
        print("Invalid choice. Exiting the game.")
        print(f"Final Scores -> Player: {player_score}, Computer: {computer_score}")
        break

    # Computer choice
    computer_choice = random.choice(choices)

    # Determine the winner
    if player_choice == computer_choice:
        print("Both choices are the same. It's a tie!")

    elif player_choice == "rock" and computer_choice == "scissors":
        print("Player wins this round!")
        player_score += 1

    elif player_choice == "paper" and computer_choice == "rock":
        print("Player wins this round!")
        player_score += 1

    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player wins this round!")
        player_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    # Display current scores
    print(f"Scores -> Player: {player_score}, Computer: {computer_score}\n")