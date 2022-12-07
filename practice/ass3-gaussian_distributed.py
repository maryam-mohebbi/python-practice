# Arrays of Random Variables

# Create a numpy array with 10000 rows and 2 columns. The first column should contain Gaussian distributed variables with mean 1 and standard deviation 2 and the second column should contain Gaussian distributed variables with mean -2 and standard deviation 0.5.

import numpy as np
from matplotlib import pyplot as plt
from numpy import random


# YOUR CODE HERE
rand_arr = np.ones(shape=(10000, 2))
first_col = random.normal(loc=1, scale=2, size=(1, 10000))
second_col = random.normal(loc=-2, scale=0.5, size=(1, 10000))
rand_arr[:, 0] = first_col
rand_arr[:, 1] = second_col

plt.hist(rand_arr[:, 0], bins=20)
plt.hist(rand_arr[:, 1], bins=20)
plt.show()
