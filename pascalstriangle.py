import numpy as np
# Get the number of rows from the user

rows = int(input("How many rows for the star triangle? "))
# Create a symmetrical triangle of stars
triangle = []
for i in range(rows):
    row = [1]
    if i > 0:
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
    triangle.append(row)
    print(' '.join(map(str, row)))
