#Author: Brett Rix

#Create a Python game of Rock Paper Scissors.
import random

#Build and use at least two custom functions:
#1. get_player_choice: This function should prompt the player, convert the response 
#to lowercase, validate the choice, and return the result.
def get_player_choice():
    choice = input("Rock, paper, or scissors? ").lower()
    while choice != "rock" and choice != "paper" and choice != "scissors":
        print(f'Sorry, "{choice}" is not a valid choice. Please try again. ')
        choice = input("Rock, paper, or scissors? ").lower()
    return choice

#2. determine_winner: This function should compare the two choices and return "win",
#"loss", or "tie".
def determine_winner():
    if player_choice == computer_choice:
        print("It's a tie! Let's go again.")
        winner = "tie"
    elif player_choice == "rock" and computer_choice == "scissors":
        print("The computer chose scissors.")
        print("You win this round!")
        winner = "win"
    elif player_choice == "paper" and computer_choice == "rock":
        print("The computer chose rock.")
        print("You win this round!")
        winner = "win"
    elif player_choice == "scissors" and computer_choice == "paper":
        print("The computer chose paper.")
        print("You win this round!")
        winner = "win"
    elif player_choice == "scissors" and computer_choice == "rock":
        print("The computer chose rock.")
        print("Computer wins this round!")
        winner = "loss"
    elif player_choice == "paper" and computer_choice == "scissors":
        print("The computer chose scissors.")
        print("Computer wins this round!")
        winner = "loss"
    elif player_choice == "rock" and computer_choice == "paper":
        print("The computer chose paper.")
        print("Computer wins this round!")
        winner = "loss"
    return winner

#Welcome the user to the game. 
print("Welcome to Rock, Paper, Scissors!")

#Ask them how many rounds they would like to play. 
rounds = int(input("How many rounds would you like to play? (Please choose an odd number) "))

#Ensure that the number they enter is an odd number so there cannot be any ties.
while rounds % 2 == 0 or rounds < 0:
    print(f"Sorry, {rounds} is not a valid choice. Please try again.")
    rounds = int(input("How many rounds would you like to play? (Please choose an odd number) "))

#Keep track of the number of wins and losses for both the player and the computer.
player_wins = 0
computer_wins = 0

#For the game play, ask the user for their choice and then generate a random 
#choice for the computer. (Note: Make sure that the user's choice is valid.) 
#If there is a tie, the game does not count, and we push to the next one. 
for i in range(rounds):
    player_choice = get_player_choice()
    random_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(random_choices)
    outcome = determine_winner()
    while outcome == "tie":
        player_choice = get_player_choice()
        computer_choice = random.choice(random_choices)
        outcome = determine_winner()
    if outcome == "loss":
        computer_wins = computer_wins + 1
    if outcome == "win":
        player_wins = player_wins + 1

#When the game play is over, determine the overall winner and print the results.
print(f"Score - You: {player_wins} | Computer: {computer_wins}")
if player_wins > computer_wins:
    print("You win!!!")
else:
    print("The computer wins!!!")
print("Thanks for playing!")
