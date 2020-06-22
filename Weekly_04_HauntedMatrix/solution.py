def matrixSum(matrix):
    try:
        nRows, nCols, s = len(matrix), len(matrix[0]), 0  # initial assignments
        ghostedColums = []  # List of columns containing 0s
        for col in range(nCols):  # each column
            for row in range(nRows):  # each row
                if matrix[row][col] == 0:
                    ghostedColums.append(col)  # the whole column is now ghosted
                elif col not in ghostedColums:
                    s += matrix[row][col]  # Add the current value to the sum
        return s
    except TypeError:  # len(matrix[0]) generates a TypeError with one dimension matrix
        return sum(matrix)  # built-in sum function


# -------------- Tests --------------
matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
# Expected Output: 9
print(matrixSum(matrix))

matrix = [1, 2, 1, 1]
# Expected Output: 5
print(matrixSum(matrix))

matrix = [[0]]
# Expected Output: 0
print(matrixSum(matrix))

matrix = [[1, 1, 1, 0],
          [0, 5, 0, 1],
          [2, 1, 3, 10]]
# Expected Output: 9
print(matrixSum(matrix))

matrix = [[1, 1, 1],
          [2, 2, 2],
          [3, 3, 3]]
# Expected Output: 18
print(matrixSum(matrix))
