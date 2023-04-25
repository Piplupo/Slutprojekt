import numpy as np

NUMBERS = (for i in range(9))

Board = np.zeros((3,3), int)

counter = 0

USED_NUMBERS = []

Player = "X"

Oponent = "O"

def random_number():
    return np.random.randint(1, 9)
def check(number):
    if number in USED_NUMBERS:
        return True
    USED_NUMBERS.append(number)
    return False

for i in range(0, 3):
    for j in range(0, 3):
        counter += 1
        Board[i,j] = counter

for i in range(3):
    for j in range(3):
        print([Board[i,j]], end="")
    print()
    
choice = input("Choose a number"):
    if choice = "1":
        np.char.replace("1", "X")
