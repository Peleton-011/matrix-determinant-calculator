
import random

# Returns x position in the grid for a specific index 
def getX(index, size):
    return index%size

# Returns y position in the grid for a specific index
def getY(index, size):
    return int(index/size) 

#Makes a random parameter to place in a slot
def randomNumber(characters):
    character = ""
    if random.randint(0, 1):
        character += "-"
    while True:
        if random.randint(0, 1):
            break
        character += str(random.randint(0, 9)
    maxlen = len(characters)
    random.randint(0,maxlen-1)
    
    
# Takes input matrix. Mode 0 is automatic
def getInput (mode = 0):
    if mode:
        return
    characters = []
    matrix = []
    dim = 4
    index = 0x61
    for i in range(dim):
        #matrix.append([])
        next
        
    j = 0
    
    while j < (0x7a - 0x60):
        characters.append(chr(index))#[getX(j, dim)].append(chr(index))
        index += 1
        j += 1
    for l in range(dim):
        matrix.append([])
    for x in range(dim*dim):
        matrix[getX(x, dim)].append(randomNumber(characters))
        
        
    
    return 
def getDeterminant():
    return
print(getInput())
