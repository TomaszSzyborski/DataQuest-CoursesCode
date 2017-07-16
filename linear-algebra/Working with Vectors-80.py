## 1. Introduction to Vectors ##

vector1 = np.asarray([4, 5, 7, 10])
vector2 = np.asarray([8, 6, 3, 2])
vector3 = np.asarray([10, 4, 6, -1])
vector1_2 = vector1 + vector2
vector3_1 = vector3 + vector1

## 2. Multiplying Vectors by Scalars ##

vector = np.asarray([4, -1, 7])
vector_7 = vector * 7
vector_8 = vector / 8

## 4. Plotting Vectors ##

import numpy as np
import matplotlib.pyplot as plt

# We're going to plot two vectors
# The first will start at origin 0,0, then go over 1 and up 2
# The second will start at origin 1,2, then go over 3 and up 2
X = [0,1]
Y = [0,2]
U = [1,3]
V = [2,2]
# Create the plot
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
# Set the x-axis limits
plt.xlim([0,6])
# Set the y-axis limits
plt.ylim([0,6])
# Show the plot
plt.show()
plt.quiver([0,1,0], [0,2,0], [1,3,4], [2,2,4], angles='xy', scale_units='xy', scale=1)
plt.xlim([0,6])
plt.ylim([0,6])
plt.show()

## 5. Determining Vector Length ##

# We're going to plot three vectors
# The first will start at origin 0,0, then go over 2 (this represents the bottom of the triangle)
# The second will start at origin 2,2, then go up 3 (this is the right side of the triangle)
# The third will start at origin 0,0, then go over 2 and up 3 (this is our vector, and the hypotenuse of the triangle)
X = [0,2,0]
Y = [0,0,0]
U = [2,0,2]
V = [0,3,3]
# Create the plot
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
plt.xlim([0,6])
plt.ylim([0,6])
plt.show()
# We can compute the length of our vector [2,3]
vector_length = (4 + 9) ** .5

## 6. Calculating the Dot Product ##

# These two vectors are orthogonal
X = [0,0]
Y = [0,0]
U = [1,-1]
V = [1,1]
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.show()
dot = 3 * 5 + 4 * 6 + 5 * 7 + 6 * 8

## 7. Making Predictions With Linear Regression ##

# We've defined slope and intercept, and loaded nba in
predictions = slope * nba["fga"] + intercept

## 9. Multiplying a Matrix by a Vector ##

import numpy as np
# Set up the coefficients as a column vector
coefs = np.asarray([[3], [-1]])
# Set up the rows we're using to make predictions
rows = np.asarray([[2,1], [5,1], [-1,1]])

# We can use np.dot to do matrix multiplication  
# This multiplies rows by coefficients
# The order is important
np.dot(rows, coefs)

nba_coefs = np.asarray([[slope], [intercept]])
nba_rows = np.vstack([nba["fga"], np.ones(nba.shape[0])]).T
predictions = np.dot(nba_rows, nba_coefs)

## 11. Applying Matrix Multiplication ##

A = np.asarray([[5,2], [3,5], [6,5]])
B = np.asarray([[3,1], [4,2]])
C = np.dot(A, B)