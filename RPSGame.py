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
def determine_winner(eleccion_de_jugador, eleccion_de_computadora):
    print(f"The computer chose {eleccion_de_computadora}.")
    if eleccion_de_jugador == eleccion_de_computadora:
        print("It's a tie! Let's go again.")
        print(" ")
        winner = "tie"
    elif eleccion_de_jugador == "rock" and eleccion_de_computadora == "scissors":
        print("You win this round!")
        print(" ")
        winner = "win"
    elif eleccion_de_jugador == "paper" and eleccion_de_computadora == "rock":
        print("You win this round!")
        print(" ")
        winner = "win"
    elif eleccion_de_jugador == "scissors" and eleccion_de_computadora == "paper":
        print("You win this round!")
        print(" ")
        winner = "win"
    elif eleccion_de_jugador == "scissors" and eleccion_de_computadora == "rock":
        print("Computer wins this round!")
        print(" ")
        winner = "loss"
    elif eleccion_de_jugador == "paper" and eleccion_de_computadora == "scissors":
        print("Computer wins this round!")
        print(" ")
        winner = "loss"
    elif eleccion_de_jugador == "rock" and eleccion_de_computadora == "paper":
        print("Computer wins this round!")
        print(" ")
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
random_choices = ["rock", "paper", "scissors"]

for i in range(rounds):
    player_choice = get_player_choice()
    computer_choice = random.choice(random_choices)
    outcome = determine_winner(player_choice, computer_choice)
    while outcome == "tie":
        player_choice = get_player_choice()
        computer_choice = random.choice(random_choices)
        outcome = determine_winner(player_choice, computer_choice)
    if outcome == "loss":
        computer_wins = computer_wins + 1
    if outcome == "win":
        player_wins = player_wins + 1

#When the game play is over, determine the overall winner and print the results.
print(" ")
print(f"Score - You: {player_wins} | Computer: {computer_wins}")
if player_wins > computer_wins:
    print("You win!!!")
else:
    print("The computer wins!!!")
print("Thanks for playing!")
print(" ")
