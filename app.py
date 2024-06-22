# Function: That simulate the game rock, paper and scissors
# Run: python app.py
# Output: The result of the game
# Input: The user choice
# Write a welcome message to the user
# Start a loop that runs 3 times
# Set the user score and the computer score to 0
# Ask the user to choose between rock, paper and scissors
# Get the user choice and set to lower case
# If user choice is not rock, paper or scissors
# Say to user choice is invalid
# Ask the user to choose between rock, paper and scissors
# Generate a random choice for the computer
# Check the user choice and the computer choice
# If the user choice is rock and the computer choice is scissors
# user wins and add 1 to the user score
# If the user choice is rock and the computer choice is paper
# computer wins and add 1 to the computer score
# If the user choice is paper and the computer choice is rock
# user wins and add 1 to the user score
# If the user choice is paper and the computer choice is scissors
# computer wins and add 1 to the computer score
# If the user choice is scissors and the computer choice is paper
# user wins and add 1 to the user score
# If the user choice is scissors and the computer choice is rock
# computer wins and add 1 to the computer score
# If the user choice is equal to the computer choice
# It's a draw
# Print the result of the game
# Print the user score
# Print the computer score
# Print the final result of the game
# If the user score is greater than the computer score
# Print that the user wins
# If the computer score is greater than the user score
# Print that the computer wins
# If the user score is equal to the computer score
# Print that it's a draw
# Ask the user if they want to play again
# If the user choice is yes
# Reset loop but score variables stay the same
# If the user choice is no
# Set variables score to 0
# Print a goodbye message
# Exit loop

import random

print("Welcome to Rock, Paper, Scissors Game!")

while True:
    user_score = 0
    computer_score = 0

    for i in range(3):
        user_choice = input("Choose between rock, paper and scissors: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice")
            user_choice = input("Choose between rock, paper and scissors: ").lower()

        computer_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice == "rock" and computer_choice == "scissors":
            print("User wins!")
            user_score += 1
        elif user_choice == "rock" and computer_choice == "paper":
            print("Computer wins!")
            computer_score += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("User wins!")
            user_score += 1
        elif user_choice == "paper" and computer_choice == "scissors":
            print("Computer wins!")
            computer_score += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("User wins!")
            user_score += 1
        elif user_choice == "scissors" and computer_choice == "rock":
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a draw!")

    print("Result of the game:")
    print("User score:", user_score)
    print("Computer score:", computer_score)

    if user_score > computer_score:
        print("User wins!")
    elif computer_score > user_score:
        print("Computer wins!")
    else:
        print("It's a draw!")

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again == "yes":
        continue
    else:
        user_score = 0
        computer_score = 0
        print("Goodbye!")
        break

# End program
