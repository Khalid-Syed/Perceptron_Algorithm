# -*- coding: utf-8 -*-
"""Perceptron Algorithm.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14LaXn_KWaCtzXNT2GPKb9z-IpWPTZSnu

### (Experimental) Random expreimentation with matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np

# Function to plot the lines
def plot_lines(x, y):
    # Plotting the original line from origin to (x, y)
    plt.plot([0, x], [0, y], label="Original Line", color="blue")

    # Midpoint of the original line
    midpoint = (x / 2, y / 2)

    # Slope of the original line (y2 - y1) / (x2 - x1) = (y - 0) / (x - 0) = y / x
    if x != 0:
        slope = y / x
        # Slope of the perpendicular (normal) line is the negative reciprocal
        normal_slope = -1 / slope
    else:
        normal_slope = 0  # Handle vertical line case (x = 0)

    # To get a normal line, we need to choose two points on it. We'll extend it in both directions
    # Line equation: (y - midpoint_y) = normal_slope * (x - midpoint_x)
    length = np.sqrt(x**2 + y**2)  # Length of the original line for scaling

    # Get two points on the normal line extending from the midpoint
    delta_x = length / 2
    if normal_slope != 0:
        delta_y = delta_x * normal_slope
    else:
        delta_y = length / 2  # For vertical normal line

    # Points on the normal line
    normal_x1, normal_y1 = midpoint[0] - delta_x, midpoint[1] - delta_y
    normal_x2, normal_y2 = midpoint[0] + delta_x, midpoint[1] + delta_y

    # Plot the normal (perpendicular) line
    plt.plot([normal_x1, normal_x2], [normal_y1, normal_y2], label="Normal Line", color="red", linestyle="--")

    # Add labels and grid
    plt.scatter([0, x], [0, y], color="green")  # Mark the origin and (x, y)
    plt.text(x, y, f"({x}, {y})", fontsize=12, ha="right")
    plt.text(0, 0, "(0, 0)", fontsize=12, ha="right")

    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Line and its Normal')
    plt.gca().set_aspect('equal', adjustable='box')

    plt.show()

# Enter the coordinate to draw a line
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

plot_lines(x, y)

"""### (Experimental) Calculating and Plotting Decision Boundary without Bias in the Perceptron"""

# import matplotlib.pyplot as plt
# import numpy as np

# # Function to plot the lines
# def plot_lines(x, y):
#     # Plotting the original line from origin to (x, y)
#     plt.plot([0, x], [0, y], label="Original Line", color="blue")

#     # Slope of the original line (y2 - y1) / (x2 - x1) = (y - 0) / (x - 0) = y / x
#     if x != 0:
#         slope = y / x
#         # Slope of the perpendicular (normal) line is the negative reciprocal
#         normal_slope = -1 / slope
#     else:
#         # Handle vertical line case (x = 0), where the normal is horizontal (slope = 0)
#         normal_slope = 0

#     # Define the length of the normal line (for plotting purposes)
#     length = np.sqrt(x**2 + y**2)  # Length of the original line as a reference

#     # If the slope is infinite (when original line is vertical), the normal line is horizontal
#     if x != 0:
#         # We want to extend the normal line by this length in both positive and negative x directions
#         normal_x1 = -length
#         normal_x2 = length
#         normal_y1 = normal_slope * normal_x1
#         normal_y2 = normal_slope * normal_x2
#     else:
#         # The normal line is horizontal when the original line is vertical
#         normal_x1 = normal_x2 = 0  # Vertical line, x remains constant
#         normal_y1 = -length
#         normal_y2 = length

#     # Plot the normal (perpendicular) line passing through the origin
#     plt.plot([normal_x1, normal_x2], [normal_y1 , normal_y2 ], label="Normal Line", color="red", linestyle="--")

#     # Add labels and grid
#     plt.scatter([0, x], [0, y], color="green")  # Mark the origin and (x, y)
#     plt.scatter([1,-2, 1.5],[1, 1, -0.5], color= "blue")
#     plt.scatter([2, -1, -2], [-2, -1.5, -1], color= "red")
#     plt.text(x, y, f"({x}, {y})", fontsize=12, ha="right")
#     plt.text(0, 0, "(0, 0)", fontsize=12, ha="right")

#     # #Question 1 coordinates
#     # plt.scatter()

#     plt.axhline(0, color='black',linewidth=0.5)
#     plt.axvline(0, color='black',linewidth=0.5)
#     plt.grid(True)
#     plt.legend()
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('Line and its Normal (through Origin)')
#     plt.gca().set_aspect('equal', adjustable='box')

#     plt.show()
#     return

# # Enter the coordinate to draw a line
# x = float(input("Enter x coordinate: "))
# y = float(input("Enter y coordinate: "))



# plot_lines(x, y)

"""### (Expreimental) Experimenting with plotting of decision boundaries"""

# import numpy as np
# import matplotlib.pyplot as plt

# # Data points (x1, x2) with labels
# points = np.array([
#     [1, 1],
#     [2, -2],
#     [-1, -1.5],
#     [-2, -1],
#     [-2, 1],
#     [1.5, -0.5]
# ])

# labels = np.array([1, -1, -1, -1, 1, 1])

# # Final weights and bias
# w = np.array([0.5, 2.5])
# b = 1

# # Plotting
# fig, ax = plt.subplots()

# # Plot data points with labels
# for i in range(len(points)):
#     if labels[i] == 1:
#         ax.scatter(points[i, 0], points[i, 1], c='blue', marker='o', label='Class +1' if i == 0 else "")
#     else:
#         ax.scatter(points[i, 0], points[i, 1], c='red', marker='x', label='Class -1' if i == 1 else "")

# # Plot the decision boundary
# x_vals = np.linspace(-3, 3, 100)
# y_vals = - (w[0] * x_vals + b) / w[1]
# ax.plot(x_vals, y_vals, 'k--', label='Decision Boundary')

# # Labels and title
# ax.set_xlabel('x1')
# ax.set_ylabel('x2')
# ax.legend(loc='best')
# ax.set_title('Perceptron Decision Boundary')

# plt.show()

"""### Perceptron Algorithm Code"""

### Perceptron Algorithm Code

import numpy as np
import matplotlib as plt

# Initializing weights and biases to zero
weights = np.array([0.0, 0.0])
bias = 0.0
no_update = 0
cycle= 0

# Dataset : [(x,y),y_label]
data = [((1, 1), 1), ((2, -2), -1), ((-1, -1.5), -1), ((-2, -1), -1), ((-2, 1), 1), ((1.5, -0.5), 1), [(-100,-100), 1]]

# Optional: Learning Rate
learning_rate = 1.0

#Method to update w and b
def upd(weights, bias, x, y):
  weights = weights + learning_rate*y*np.array(x)
  bias = bias + learning_rate * y
  return weights, bias

def perceptron_algorithm(w, b, data, no_update):

  for (x,y) in data:
    y_pred = np.dot(w,x) + b
    if y_pred < 0:
      sign = -1
    else:
      sign = 1

    if sign != y:
      w,b= upd(w, b, x, y)
    else:
      no_update= no_update + 1

  return w, b, no_update

while ((no_update != len(data)) and (cycle <= 5)):
  no_update = 0
  weights, bias, no_update = perceptron_algorithm(weights, bias, data, no_update)
  cycle+= 1

if no_update == len(data):
  print('The model has converged!')

else:
       print('The model didn\'t converge before the set limit. This data is linearly inseparable.')

print('For the points {0},\n The weights are {1} and the biases are {2}. Final cycle is {3}'.format(data,weights, bias, cycle))

"""### Code with bias for perceptron decision boundary plotting



"""

# Code with bias for perceptron decision boundary plotting

import matplotlib.pyplot as plt
import numpy as np

data = [((1, 1), 1), ((2, -2), -1), ((-1, -1.5), -1), ((-2, -1), -1), ((-2, 1), 1), ((1.5, -0.5), 1)]

# Function to plot the lines including the bias term
def plot_lines(x, y, bias):
    # Plotting the original line from origin to (x, y)
    plt.plot([0, x], [0, y], label="Weight Vector", color="blue")

    # Slope of the original line (y2 - y1) / (x2 - x1) = (y - 0) / (x - 0) = y / x
    if x != 0:
        slope = y / x
        # Slope of the perpendicular (normal) line is the negative reciprocal
        normal_slope = -1 / slope
    else:
        # Handle vertical line case (x = 0), where the normal is horizontal (slope = 0)
        normal_slope = 0

    # Define the length of the normal line (for plotting purposes)
    length = np.sqrt(x**2 + y**2)  # Length of the original line as a reference

    # If the slope is infinite (when original line is vertical), the normal line is horizontal
    if x != 0:
        # We want to extend the normal line by this length in both positive and negative x directions
        normal_x1 = -length
        normal_x2 = length
        normal_y1 = normal_slope * normal_x1
        normal_y2 = normal_slope * normal_x2
    else:
        # The normal line is horizontal when the original line is vertical
        normal_x1 = normal_x2 = 0  # Vertical line, x remains constant
        normal_y1 = -length
        normal_y2 = length

    # Plot the normal (perpendicular) line passing through the origin
    #plt.plot([normal_x1, normal_x2], [normal_y1 , normal_y2 ], label="Normal Line", color="red", linestyle="--")

    # Plotting the decision boundary (taking bias into account)
    # Decision boundary: w1 * x1 + w2 * x2 + bias = 0
    # Rearranging: x2 = - (w1 / w2) * x1 - (bias / w2)

    # Create points for x-axis range (for decision boundary)
    x_vals = np.linspace(-3, 3, 100)

    # Ensure that w2 is not zero to avoid division by zero
    if y != 0:
        decision_y_vals = - (x / y) * x_vals - (bias / y)
        plt.plot(x_vals, decision_y_vals, label="Decision Boundary", color="orange", linestyle="--")
    else:
        # If y is zero, the decision boundary is vertical
        plt.axvline(-bias / x, color="orange", linestyle="--", label="Decision Boundary")

    # Add labels and grid
    plt.scatter([0, x], [0, y], color="green")  # Mark the origin and (x, y)
    plt.scatter([1, -2, 1.5], [1, 1, -0.5], color="blue")
    plt.scatter([2, -1, -2], [-2, -1.5, -1], color="red")
    plt.text(x, y, f"({x}, {y})", fontsize=12, ha="right")
    plt.text(0, 0, "(0, 0)", fontsize=12, ha="right")

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Weight vector and Decision Boundary (with Bias)')
    plt.gca().set_aspect('equal', adjustable='box')

    plt.show()
    return

# Enter the coordinate and bias to draw a line
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
bias = float(input("Enter bias: "))

plot_lines(x, y, bias)

0