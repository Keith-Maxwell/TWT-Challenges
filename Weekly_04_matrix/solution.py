def matrixSum(matrix):
    try:
        nRows, nCols, s = len(matrix), len(matrix[0]), 0  # initial assignments
        for col in range(nCols):  # for each column
            for row in range(nRows):  # for each row
                if (matrix[row-1][col] != 0) or (row == 0):  # no zero above or the first row
                    s += matrix[row][col]  # add the number to the sum
        return s
    except TypeError:  # len(matrix[0]) generates a TypeError with one dimension matrix
        return sum(matrix)  # built-in sum function


# For
matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
# the output should be
print(matrixSum(matrix))  # = 9

matrix2 = [1, 2, 1, 1]
print(matrixSum(matrix2))  # = 5
