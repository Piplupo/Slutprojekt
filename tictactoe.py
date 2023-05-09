import numpy as np

NUMBERS = [i + 1 for i in range(9)]

Board = np.zeros((3,3), str)

counter = 0

USED_NUMBERS = []

Player = "X"

Oponent = "O"

O = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

def oponents_turn():
    O[random.randint(0, len(O))]

for i in range(0, 3):
    for j in range(0, 3):
        counter += 1
        Board[i,j] = counter

def write():
    for i in range(3):
        for j in range(3):
            print([Board[i,j]], end="")
        print()
    
choice = int(input("Choose a number: "))
if choice == 1:
    # return np.char.replace("1", "1X")
    Board[0][0] = "X"
elif choice == 2:
    Board[0][1] = "X"
elif choice == 3:
    Board[0][2] = "X"
elif choice == 4:
    Board[1][0] = "X"
elif choice == 5:
    Board[1][1] = "X"
elif choice == 6:
    Board[1][2] = "X"
elif choice == 7:
    Board[2][0] = "X"
elif choice == 8:
    Board[2][1] = "X"
elif choice == 9:
    Board[2][2] = "X"

oponents_turn = True
if oponents_turn == "1":
   Board[0][0] = "O"
elif oponents_turn == "2":
    Board[0][1] = "O"
elif oponents_turn == "3":
    Board[0][2] = "O"
elif oponents_turn == "4":
    Board[1][0] = "O"
elif oponents_turn == "5":
    Board[1][1] = "O"
elif oponents_turn == "6":
    Board[1][2] = "O"
elif oponents_turn == "7":
    Board[2][0] = "O"
elif oponents_turn == "8":
    Board[2][1] = "O"
elif oponents_turn == "9":
    Board[2][2] = "O"
write()