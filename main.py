import random


# Returns x position in the grid for a specific index
def getX(index, size):
    return index % size


# Returns y position in the grid for a specific index
def getY(index, size):
    return int(index / size)


# Makes a random parameter to place in a slot
def randomNumber(characters):
    character = ""
    maxlen = len(characters) - 1

    # Randomly choose the sign of the number
    if random.randint(0, 1):
        character += "-"

    # Randomly add a number to the parameter
    while random.randint(0, 1):
        character += str(random.randint(0, 9))

    # Add a random character to the parameter
    character += characters[random.randint(0, maxlen)]


# Makes randomly generated matrix
def makeInput(size=random.randint(2, 5)):
    matrix = []
    characters = []
    index = 0x61
    j = 0

    # Make legal character list
    for j in range(0x7a - 0x60):
        characters.append(chr(index + j))  # [getX(j, dim)].append(chr(index))

    # Make all columns of the matrix
    for i in range(size):
        matrix.append([])

    # Make a random number for each cell
    for x in range(size * size):
        matrix[getX(x, size)].append(randomNumber(characters))

    return matrix


# Takes input matrix.
def getInput():
    matrix = []
    size = int(input("What size is the matrix? "))

    # Make all columns for the input matrix
    for i in range(size):
        matrix.append([])

    # Ask for each cell's value individually
    for i in range(size * size):
        inputPrompt = "Insert cell " + str(getX(i, size)) + " , " + str(getY(i, size))
        matrix[getX(i, size)].append(input(inputPrompt))

    return [matrix, size]


def getDeterminant():
    return

print(makeInput())
