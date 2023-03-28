import numpy as np

Board = np.zeros((3,3), int)

counter = 0

for i in range(0, 3):
    for j in range(0, 3):
        counter += 1
        Board[i,j] = counter

for i in range(3):
    for j in range(3):
        print([Board[i,j]], end="")
    print()