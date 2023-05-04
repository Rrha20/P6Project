import numpy as np
from scipy.spatial.transform import Rotation

# Define the center point
x0, y0, z0 = 0, 0, 0

# Define the number of functions and the minimum angle between vectors
num_functions = 10
min_angle = np.pi / (num_functions + 1)

# Generate a spherical Fibonacci sequence of unit vectors
theta = np.pi * (3 - np.sqrt(5))
points = np.zeros((num_functions, 3))
points[:, 2] = np.linspace(1 - 1 / num_functions, 1 / num_functions - 1, num_functions)
r = np.sqrt(1 - points[:, 2] ** 2)
phi = np.mod(np.arange(num_functions), num_functions) * theta
points[:, 0] = r * np.cos(phi)
points[:, 1] = r * np.sin(phi)
points = Rotation.from_euler('yx', [-90, 0], degrees=True).apply(points)

# Define the threshold distance
threshold = 1

# Generate the functions
functions = []
Coeefs = []
for i in range(num_functions):
    # Choose a unit vector
    vector = points[i]

    # Generate a function
    a, b, c = np.random.normal(size=3)
    direction = np.array([a, b, c])
    direction /= np.linalg.norm(direction)
    distance = np.abs(np.dot(direction, [x0, y0, z0]) ) / np.linalg.norm(direction)
    if distance > threshold:
        direction *= threshold / distance
        distance = threshold
    fi = f"0 = {direction[0]:.3f}x + {direction[1]:.3f}y + {direction[2]:.3f}z"
    functions.append(fi)
    function_coeffs = [direction[0], direction[1], direction[2]]
    Coeefs.append(function_coeffs)

for i in functions:
    print(i)
for i in Coeefs:
    print(str(i) + ", ")
