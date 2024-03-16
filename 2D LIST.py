# Two-dimensional lists, often referred to as
# 2D lists or matrices, are a fundamental data structure in Python.
# At their core, they are lists of lists, and this concept opens up
# a world of possibilities for organizing and manipulating data.

# example:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print(matrix[0][1])
pass

# example2
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)
