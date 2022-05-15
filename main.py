import random


# Returns x position in the grid for a specific index
def getX(index, size):
    return index % size


# Returns y position in the grid for a specific index
def getY(index, size):
    return int(index / size)


# Makes a random parameter to place in a slot
def randomNumber(characters):
    hasNumber = False
    character = ""
    maxlen = len(characters) - 1

    if not random.randint(0, 3):
        return "0"
    # Randomly choose the sign of the number
    if random.randint(0, 1):
        character += "-"

    # Randomly add a number to the parameter
    while random.randint(0, 1):
        newNum = str(random.randint(0, 9))
        if (newNum == "0") and (not hasNumber):
            continue
        hasNumber = True
        character += newNum

    # Add a random character to the parameter
    if random.randint(0, 1) or (not hasNumber):
        character += characters[random.randint(0, maxlen)]

    return character


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

    return [matrix, size]


# Takes input matrix.
def getInput():
    matrix = []
    size = int(input("What size is the matrix? "))

    # Make all columns for the input matrix
    for i in range(size):
        matrix.append([])

    # Ask for each cell's value individually
    for i in range(size * size):
        inputPrompt = "Insert cell " + str(getX(i, size)) + " , " + str(getY(i, size)) + ": "
        matrix[getX(i, size)].append(input(inputPrompt))

    return [matrix, size]


def multiply(items):
    result = "("
    for i in range(len(items)):
        if items[i] == "0":
            return "0"
        result += str(items[i]) + " * "
    result = result[:-3]
    result += ")"
    return result


def getDeterminant(matrix=[]):
    if not matrix:
        pack = makeInput(3)
        print(pack)
        matrix = pack[0]
        size = pack[1]
    else:
        size = len(matrix[0])
    result = ""

    # Solves a 2x2 determinant

    if size < 3:
        resultPart1 = "( " + multiply([matrix[0][0], matrix[1][1]]) + " - "
        resultPart2 = multiply([matrix[1][0], matrix[0][1]]) + " )"
        result += resultPart1 + resultPart2
        return result

    # Solves any determinant recursively

    for subDet in range(size):

        # If the subdeterminant number is 0 ignore that subdeterminant
        if matrix[subDet][0] == "0":
            continue

        # Creates the subdeterminant matrix
        tinyDet = []

        if (subDet % 2) == 1:
            result += " -"
        else:
            result += " +"
        result += matrix[subDet][0] + "("

        for i in range(size):
            column = []
            if i == subDet:
                continue
            for j in range(size - 1):
                column.append(matrix[i][j + 1])
            tinyDet.append(column)
        print("tinyDET:")
        print(tinyDet)
        result += getDeterminant(tinyDet)

    # result.append(matrix[subDet][0] + " * (" + getDeterminant(tinyDet) )
    return result


print(getDeterminant())
