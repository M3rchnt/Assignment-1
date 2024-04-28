def matrixMultiplyFor(matrix1, matrix2):
    # Input 2 matrices, return product of matrices
    assert (len(matrix1) == len(matrix2[0])) or (len(matrix2) == len(matrix1[0])) # Assertion that the matrices ARE valid to be multiplied. The rows of one matrix (len(matrix1)) MUST match the columns (len(matrix2[0])) of the other.
    # Case insensitive, if matrixes are able to be multiplied when placed in the opposite orientation then the code will still run
    matrixProduct = [] # Initialize return matrix
    if len(matrix1[0]) == len(matrix2): # Check to see if matrix1 columns match matrix2 rows
        for i in range(0, len(matrix1), 1): # For loops to multiply the matrices
            matrixProduct.append([])
            for j in range(0, len(matrix2[0]), 1):
                sum = 0
                for k in range(0, len(matrix1[0]), 1):
                    sum += matrix1[i][k] * matrix2[k][j] # Mathematical statement used in determining matrix multiplication
                matrixProduct[i].append(sum)
    elif len(matrix2[0]) == len(matrix1): # Check to see if matrix2 columns match matrix1 rows
        for i in range(0, len(matrix2), 1): # For loops to multiply the matrices
            matrixProduct.append([])
            for j in range(0, len(matrix1[0]), 1):
                sum = 0
                for k in range(0, len(matrix2[0]), 1):
                    sum += matrix2[i][k] * matrix1[k][j] # Mathematical statement used in determining matrix multiplication
                matrixProduct[i].append(sum)
    return matrixProduct    

def matrixMultiplyWhile(matrix1, matrix2):
    # Input 2 matrices, return product of matrices
    assert (len(matrix1) == len(matrix2[0])) or (len(matrix2) == len(matrix1[0])) # Assertion that the matrices ARE valid to be multiplied. The rows of one matrix (len(matrix1)) MUST match the columns (len(matrix2[0])) of the other.
    # Case insensitive, if matrixes are able to be multiplied when placed in the opposite orientation then the code will still run
    matrixProduct = [] # Initialize return matrix
    if len(matrix1[0]) == len(matrix2): # Check to see if matrix1 columns match matrix2 rows
        i = 0
        while (i < len(matrix1)): # While loops to multiply the matrices
            matrixProduct.append([])
            j = 0
            while (j < len(matrix2[0])):
                sum = 0
                k = 0
                while (k < len(matrix1[0])):
                    sum += matrix1[i][k] * matrix2[k][j] # Mathematical statement used in determining matrix multiplication
                    k += 1 # Incrementing counter to progress in list
                matrixProduct[i].append(sum)
                j += 1
            i += 1
    elif len(matrix2[0]) == len(matrix1): # Check to see if matrix2 columns match matrix1 rows
        i = 0
        while (i < len(matrix2)): # While loops to multiply the matrices
            matrixProduct.append([])
            j = 0
            while (j < len(matrix1[0])):
                sum = 0
                k = 0
                while (k < len(matrix2[0])):
                    sum += matrix2[i][k] * matrix1[k][j] # Mathematical statement used in determining matrix multiplication
                    k += 1 # Incrementing counter to progress in list
                matrixProduct[i].append(sum)
                j += 1
            i += 1
    return matrixProduct

# Initializing matrices to be multiplied
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11,12], [1,1]]

print("Contents of matrix1: ")
for i in matrix1:
    for j in i:
        print(f"{j} ", end="")
    print("")

print("Contents of matrix2: ")
for i in matrix2:
    for j in i:
        print(f"{j} ", end="")
    print("")
# Testing code
product = matrixMultiplyFor(matrix1, matrix2)

print("Contents of product matrix (for loop): ")
for i in product:
    for j in i:
        print(f"{j} ", end="")
    print("")

product = matrixMultiplyWhile(matrix1, matrix2)

print("Contents of product matrix (while loop): ")
for i in product:
    for j in i:
        print(f"{j} ", end="")
    print("")

