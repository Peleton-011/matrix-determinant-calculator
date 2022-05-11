
# Returns x position in the grid for a specific index 
def getX(index, size):
    return index%size

# Returns y position in the grid for a specific index
def getY(index, size):
    return int(index/size) 

# Takes input matrix. Mode 0 is automatic
def getInput (mode = 0):
    if mode:
        return
    matrix = []
    dim = 4
    index = 0x61
    for i in range(dim):
        matrix.append([])
        
    for j in range(dim*dim):
        
        matrix[getX(j, dim)].append(chr(index))
        index += 1
    
    return matrix
def getDeterminant():
    return
print(getInput())
