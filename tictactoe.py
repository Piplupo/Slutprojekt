import numpy as np
import random

NUMBERS = [i + 1 for i in range(9)]

Board = np.zeros((3, 3), str)

counter = 0

USED_NUMBERS = []

Player = "X"
Opponent = "O"

O = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def oponents_turn():
    return random.choice(O)

for i in range(0, 3):
    for j in range(0, 3):
        counter += 1
        Board[i, j] = counter

def write():
    for i in range(3):
        for j in range(3):
            print([Board[i, j]], end="")
        print()
        
def win():
    if Board[0][0] == Board[0][1] == Board[0][2] == "X":
        print ("You win!")
    elif Board[1][0] == Board[1][1] == Board[1][2] == "X":
        print ("You win!")
    elif Board[2][0] == Board[2][1] == Board[2][2] == "X":
        print ("You win!")
    elif Board[0][0] == Board[1][0] == Board[2][0] == "X":
        print ("You win!")
    elif Board[0][1] == Board[1][1] == Board[2][1] == "X":
        print ("You win!")
    elif Board[0][2] == Board[1][2] == Board[2][2] == "X":
        print ("You win!")
    elif Board[0][0] == Board[1][1] == Board[2][2] == "X":
        print ("You win!")
    elif Board[0][2] == Board[1][1] == Board[2][0] == "X":
        print ("You win!")

def loss():
    if Board[0][0] == Board[0][1] == Board[0][2] == "O":
        print ("You lose!")
    elif Board[1][0] == Board[1][1] == Board[1][2] == "O":
        print ("You lose!")
    elif Board[2][0] == Board[2][1] == Board[2][2] == "O":
        print ("You lose!")
    elif Board[0][0] == Board[1][0] == Board[2][0] == "O":
        print ("You lose!")
    elif Board[0][1] == Board[1][1] == Board[2][1] == "O":
        print ("You lose!")
    elif Board[0][2] == Board[1][2] == Board[2][2] == "O":
        print ("You lose!")
    elif Board[0][0] == Board[1][1] == Board[2][2] == "O":
        print ("You lose!")
    elif Board[0][2] == Board[1][1] == Board[2][0] == "O":
        print ("You lose!")
    
    
while True:
    choice = int(input("Choose a number: "))
    if choice == 1:
        if Board[0][0] == "O":
            print ("Number taken, choose another please")
            continue
        Board[0][0] = "X"
    elif choice == 2:
        if Board[0][1] == "O":
            print ("Number taken, choose another please")
            continue
        Board[0][1] = "X"
    elif choice == 3:
        if Board[0][2] == "O":
            print ("Number taken, choose another please")
            continue
        Board[0][2] = "X"
    elif choice == 4:
        if Board[1][0] == "O":
            print ("Number taken, choose another please")
            continue
        Board[1][0] = "X"
    elif choice == 5:
        if Board[1][1] == "O":
            print ("Number taken, choose another please")
            continue
        Board[1][1] = "X"
    elif choice == 6:
        if Board[1][2] == "O":
            print ("Number taken, choose another please")
            continue
        Board[1][2] = "X"
    elif choice == 7:
        if Board[2][0] == "O":
            print ("Number taken, choose another please")
            continue
        Board[2][0] = "X"
    elif choice == 8:
        if Board[2][1] == "O":
            print ("Number taken, choose another please")
            continue
        Board[2][1] = "X"
    elif choice == 9:
        if Board[2][2] == "O":
            print ("Number taken, choose another please")
            continue
        Board[2][2] = "X"
    win()

    
    oponents_turn_choice = oponents_turn()

    if oponents_turn_choice == 1:
        if Board[0][0] == "X":
            oponents_turn
            continue
        Board[0][0] = "O"
    elif oponents_turn_choice == 2:
        if Board[0][1] == "X":
            oponents_turn
            continue
        Board[0][1] = "O"
    elif oponents_turn_choice == 3:
        if Board[0][2] == "X":
            oponents_turn
            continue
        Board[0][2] = "O"
    elif oponents_turn_choice == 4:
        if Board[1][0] == "X":
            oponents_turn
            continue
        Board[1][0] = "O"
    elif oponents_turn_choice == 5:
        if Board[1][1] == "X":
            oponents_turn
            continue
        Board[1][1] = "O"
    elif oponents_turn_choice == 6:
        if Board[1][2] == "X":
            oponents_turn
            continue
        Board[1][2] = "O"
    elif oponents_turn_choice == 7:
        if Board[2][0] == "X":
            oponents_turn
            continue
        Board[2][0] = "O"
    elif oponents_turn_choice == 8:
        if Board[2][1] == "X":
            oponents_turn
            continue
        Board[2][1] = "O"
    elif oponents_turn_choice == 9:
        if Board[2][2] == "X":
            oponents_turn
            continue
        Board[2][2] = "O"
    loss()

    write()