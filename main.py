import random
from copy import deepcopy

yep = ["Y", "y"]
nope = ["N", "n"]


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
def makeInput(size=0):
    if not size:
        mode = input("Do you want to select a size? (Y/N)")

        if mode in yep:
            size = int(input("Enter size: "))
        elif mode in nope:
            size = random.randint(2, 6)
        else:
            print("Learn to choose please...")
            size = 6

    matrix = []
    characters = []
    index = 0x61

    # Make legal character list
    for j in range(0x7a - 0x60):
        characters.append(chr(index + j))  # [getX(j, dim)].append(chr(index))

    # Make all columns of the matrix
    for i in range(size):
        matrix.append([])

    # Make a random number for each cell
    for x in range(size * size):
        matrix[getX(x, size)].append(randomNumber(characters))

    # print(matrix)
    return [matrix, size]


# Takes input matrix.
def getInput():
    matrix = []
    solutionMatrix = []

    size = int(input("What size is the matrix? "))

    mode = input("Do you want to add a result matrix to solve an equation system? (Y/N)")

    if mode in yep:
        for i in range(size):
            solutionElement = str(input("Insert solution matrix element Y = " + str(i) + ": "))
            solutionMatrix.append(solutionElement)
    elif not (mode in nope):
        print("Learn to choose please...")
        return makeInput(6)



    # Make all columns for the input matrix
    for i in range(size):
        matrix.append([])

    # Ask for each cell's value individually
    for i in range(size * size):
        inputPrompt = "Insert cell " + str(getX(i, size)) + " , " + str(getY(i, size)) + ": "
        matrix[getX(i, size)].append(input(inputPrompt))

    print("This is your matrix: ")
    print(matrix)
    if not solutionMatrix:
        return [matrix, size]
    return [matrix, size, solutionMatrix]


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
    #print("Matrix:\n")
    #print(matrix)
    #print("\n")
    if not matrix:
        mode = input("Do you want to insert a matrix? (Y/N)")
        if mode in yep:
            pack = getInput()
        elif mode in nope:
            pack = makeInput()
            #print(pack)
        else:
            print("Learn to choose please...")
            pack = makeInput(4)
        matrix = pack[0]
        size = pack[1]
        result = "This is the result: \n"
    else:
        size = len(matrix[0])
        result = ""

    # Solves a 2x2 determinant

    if size < 3:
        resultPart1 = multiply([matrix[0][0], matrix[1][1]])
        resultPart2 = multiply([matrix[1][0], matrix[0][1]])
        if (resultPart1 == "0") and (resultPart2 == "0"):
            return "0"
        result += resultPart1 + " - " + resultPart2
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
        result += str(matrix[subDet][0])

        for i in range(size):
            column = []
            if i == subDet:
                continue
            for j in range(size - 1):
                column.append(matrix[i][j + 1])
            tinyDet.append(column)
        # print("tinyDET:")
        # print(tinyDet)
        result += "[" + getDeterminant(tinyDet) + "]"

    # result.append(matrix[subDet][0] + " * (" + getDeterminant(tinyDet) )
    result = result.replace("--", "+")
    result = result.replace("+-", "-")
    result = result.replace("-+", "-")
    return result


# Solves a system of equations using the Cramer method
def solveEquation(matrix=[]):
    if not matrix:
        mode = input("Do you want to insert a matrix? (Y/N)")
        if mode in yep:
            pack = getInput()
        elif mode in nope:
            pack = makeInput()

            # Gets another random matrix of the same size to take a column as result
            pack.append(makeInput(len(pack[0])))
            print(pack[0])
            print(" = ")
            print(pack[2])
        else:
            print("Learn to choose please...")
            pack = makeInput(4)
        matrix = pack[0]
        size = pack[1]
        resultMatrix = pack[2]
        returnText = "This is the result: \n \n"
    else:
        size = len(matrix[0])
        resultMatrix = matrix[2]
        matrix = matrix[0]
        returnText = ""

    denominator = getDeterminant(matrix)

    numerators = []

    for i in range(size):
        tempMatrix = deepcopy(matrix)
        tempMatrix[i] = resultMatrix
        numerators.append(getDeterminant(tempMatrix))
        print(tempMatrix)

    for i in range(size):
        returnText += " Var " + str(i + 1) + ":\n \n"
        returnText += str(numerators[i]) + "\n"
        if len(numerators[i]) > len(denominator):
            divisionLength = len(numerators[i])
        else:
            divisionLength = len(denominator)

        for j in range(divisionLength):
            returnText += "-"
        returnText += "\n" + denominator + "\n \n"

    return returnText

# Main function, handles everything
def main():
    inputs = getInput()
    #print("len")
    #print(len(inputs))
    if len(inputs) > 2:
        return solveEquation(inputs)
    else:
        return getDeterminant(inputs)


print(main())