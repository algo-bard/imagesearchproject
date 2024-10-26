
import random
from platform import machine
from tokenize import endpats

print("Welcome to Rock, Paper, Scissors")

print("What would you like to play?")
print("R for Rock")
print("P for Paper")
print("S for Scissors")


while True:
    # Variables
    RSelect = "R"
    PSelect = "P"
    SSelect = "S"

    print("Enter your choice")

    userselect = input()
    machineselect = random.choice([RSelect, PSelect, SSelect])

    computerselect = ""

    if machineselect == RSelect:
        computerselect = "Rock"
    elif machineselect == PSelect:
        computerselect = "Paper"
    elif machineselect() == SSelect:
        computerselect = "Scissors"

    print("Computer selected " + computerselect)
    # Computer wins
    if userselect == "R" and machineselect == PSelect:
        print("Computer wins!")
    elif userselect == "P" and machineselect == SSelect:
        print("Computer wins!")
    elif userselect == "S" and machineselect == RSelect:
        print("Computer wins!")

    # User Wins
        print("User wins!")
    elif userselect == "P" and machineselect == RSelect:
        print("User wins!")
    elif userselect == "S" and machineselect == PSelect:
        print("User wins!")

    # Tied games
    elif userselect ==  machineselect:
        print("Its a tie!")
    else:
        print("Invalid input.")

