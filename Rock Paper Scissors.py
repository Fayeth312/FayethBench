user1 = input("Player 1; rock, paper or scissors?: ")
user2 = input("Player 2; rock, paper or scissors?: ")

if  user1 == "Rock" or user1 == "rock": 
    if user2 == "paper" or user2 == "Paper":
        print("Player 2 wins!")
    elif user2 == "scissors" or user2 == "Scissors": 
        print("Player 1 wins!")
    elif user2 == "Rock" or user2 == "rock":
        print("Error, try again")

if  user1 == "Paper" or user1 == "paper": 
    if user2 == "Scissors" or user2 == "scissors":
        print("Player 2 wins!")
    elif user2 == "Rock" or user2 == "rock": 
        print("Player 1 wins!")
    elif user2 == "Paper" or user2 == "paper":
        print("Error, try again")

if  user1 == "Scissors" or user1 == "scissors": 
    if user2 == "Rock" or user2 == "rock":
        print("Player 2 wins!")
    elif user2 == "Paper" or user2 == "paper": 
        print("Player 1 wins!")
    elif user2 == "Paper" or user2 == "paper":
        print("Error, try again")