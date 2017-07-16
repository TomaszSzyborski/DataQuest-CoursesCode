## 2. Systems of Equations as Matrices ##

import numpy as np

# Set the dtype to float to do float math with the numbers
matrix = np.asarray([
    [2, 1, 25],
    [3, 2, 40]  
], dtype=np.float32)
# Multiply the first row by 2
matrix[0] *= 2

# Subtract the second row from the first row
matrix[0] -= matrix[1]

# Subtract 3 times the first row from the second row
matrix[1] -= (3 * matrix[0])

# Divide the second row by 2
matrix[1] /= 2

## 4. Solving More Complex Equations ##

import numpy as np

matrix = np.asarray([
    [1, 2, 0, 7],
    [0, 3, 3, 11],
    [1, 2, 2, 11]
], dtype=np.float32)
# Subtract the first row from the third row
matrix[2] -= matrix[0]

# Divide the third row by 2
matrix[2] /= 2

# Subtract 3 times the third row from the second row
matrix[1] -= (matrix[2] * 3)

# Divide the second row by 3
matrix[1] /= 3

# Subtract 2 times the second row from the first row
matrix[0] -= (2 * matrix[1])

## 5. Putting a Matrix into Echelon Form ##

matrix = np.asarray([
    [0, 0, 0, 7],
    [0, 0, 1, 11],
    [1, 2, 2, 11],
    [0, 5, 5, 1]
], dtype=np.float32)

# Swap the first and the third rows; first swap
matrix[[0,2]] = matrix[[2,0]]
# Second swap
matrix[[1,3]] = matrix[[3,1]]

# Third swap
matrix[[2,3]] = matrix[[3,2]]

## 6. Reduced Row Echelon Form ##

A = np.asarray([
        [0, 2, 1, 5],
        [1, 2, 1, 8],
        [3, 0, 1, 10],
        ], dtype=np.float32)

# First, we'll swap the second row with the first to get a non-zero coefficient in the first column
A[[0,1]] = A[[1,0]]

# The leading coefficient is already 1, so we don't need to divide
# Now, we need to make sure that our 1 coefficient is the only coefficient in its column
# We have to subtract 3 times the first row from the third row
A[2] -= 3 * A[0]

# Now, we move to row two
# We divide by 2 to get a 1 as the leading coefficient
A[1] /= 2

# We subtract 2 times the second row from the first to get rid of
# the second column coefficient in the first row
A[0] -= 2 * A[1]

# And we'll add 6 times the second row to the third to eliminate the leading coefficient there
A[2] += 6 * A[1]

# Now we can move to the third row where the leading coefficient is already 1
# We just need to subtract half of the third from the second
A[1] -= 0.5 * A[2]

# We've solved our system!
print(A)

## 7. Inconsistent Systems are Unsolvable ##

A = np.asarray([
    [10, 5, 20, 60],
    [3, 1, 0, 11],
    [8, 2, 2, 30],
    [0, 4, 5, 13]
], dtype=np.float32)

B = np.asarray([
    [5, -1, 3, 14],
    [0, 1, 2, 8],
    [0, -2, 5, 1],
    [0, 0, 6, 6]
], dtype=np.float32)
# Divide the first row by 10
A[0] /= 10

# Subtract 3 times the first row from the second
A[1] -= (3 * A[0])

# Subtract 8 times the first row from the third
A[2] -= (8 * A[0])

# Multiply the second row by -2
A[1] *= -2

# Subtract .5 times the second row from the first
A[0] -= (A[1] * .5)

#  Subtract -2 times the second row from the third
A[2] -= (A[1] * -2)

# Subtract 4 times the second row from the fourth
A[3] -= (A[1] * 4)

# Divide the third row by 10
A[2] /= 10

# Subtract -4 times the third row from the first
A[0] -= (A[2] * -4)

# Subtract 12 times the third row from the second
A[1] -= (A[2] * 12)

# Subtract the third row times -43 from the fourth
A[3] -= (A[2] * -43)

# A is in row echelon form, and we have a unique solution, so it is consistent
A_consistent = True

# Divide the fourth row by 6
B[3] /= 6

# Subtract -2 times the second row from the third row
B[2] -= (B[1] * -2)

# Divide the third row by 9
B[2] /= 9

# The last variable (z) cannot simultaneously equal 1.88 and 1, so B is inconsistent
B_consistent = False

## 8. Complex Systems Can Have Infinite Solutions ##

A = np.asarray([
        [2, 4, 8, 20],
        [4, 8, 16, 40],
        [20, 5, 5, 10]
], dtype=np.float32)

B = np.asarray([
        [1, 1, 1, 4],
        [3, -2, 5, 8],
        [8, -4, 5, 10]
        ], dtype=np.float32)
# Divide the first row in A by 2
A[0] /= 2

# Subtract the first row times 4 from the second row
# This zeros out the row
A[1] -= (A[0] * 4)

# Subtract the first row times 20 from the last row
A[2] -= (A[0] * 20)

# Now we're stuck; we can't simplify A any more, so it has infinite solutions
A_infinite = True

# B -- Subtract the first row times 3 from the second row
B[1] -= (B[0] * 3)

# Subtract the first row times 8 from the third row
B[2] -= (B[0] * 8)

# Divide the second row by -5
B[1] /= -5

# Subtract the second row from the first
B[0] -= B[1]

# Subtract the second row times -12 from the third row
B[2] -= (B[1] * -12)

# Divide the last row by -7.8 (the third column element)
B[2] /= B[2,2]

# Subtract the third row times the third column of the first row from the first row
B[0] -= (B[2] * B[0][2])

# Subtract the third row times the third column of the second row from the second row
B[1] -= (B[2] * B[1][2])

# We can solve B, which has a single solution, not infinitely many
B_infinite = False