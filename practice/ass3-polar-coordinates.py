# Polar Coordinates

# Let  𝑃=(𝑥,𝑦)  be a point in the standard 2D-space. Its cartesian coordinates can be converted into polar coordinates by applying the transformations:

# 𝑟=√𝑥^2+𝑦^2
# for the radius  𝑟  and

# 𝜑=𝑡𝑎𝑛−1(𝑦𝑥)
# for the angle  𝜑

# Create a random 10x2 matrix representing cartesian coordinates and convert them to polar.


import numpy as np

# YOUR CODE HERE

coordinate = np.random.randint(-100, 100, (10, 2))


def coordinate_to_polar(list):
    polar_list = []
    x = list[:, 0]
    y = list[:, 1]
    radius = np.sqrt(x**2 + y**2)
    angle = np.arctan2(y, x)
    for i in range(len(list)):
        polar_list.append([radius[i], angle[i]])
    return np.array(polar_list)


print(coordinate)
print(coordinate_to_polar(coordinate))

# AI Test
# # Create a random 10x2 matrix representing cartesian coordinates
# cartesian = np.random.rand(10, 2)

# # Convert the cartesian coordinates to polar
# polar = np.empty_like(cartesian)
# polar[:, 0] = np.sqrt(np.sum(cartesian**2, axis=1))  # r
# polar[:, 1] = np.arctan2(cartesian[:, 1], cartesian[:, 0])  # theta

# # Print the polar coordinates
# print(polar)
