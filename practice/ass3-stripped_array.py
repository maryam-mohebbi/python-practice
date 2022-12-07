# Indexing 2D Arrays

# Write a function that takes a 2D array as an argument with at least 3 rows and 3 columns (throw an exception, if the user provides too few dimensions). The matrix is then stripped of the 'outer' rows and columns and only the remaining inner matrix is returned. Below a visual example for a 4x5 matrix:

# ⋅⋅⋅⋅⋅𝑂𝑂⋅⋅𝑂𝑂⋅⋅𝑂𝑂⋅⋅⋅⋅⋅

# Test your function for the matrix below. Don't forget to write the docstrings.

import numpy as np


def strip_mat(arr):
    # YOUR CODE HERE
    if len(arr) < 3 or len(arr[0]) < 3:
        raise ValueError('Your Matrix is too small')
    else:
        updated_arr = np.delete(arr, 0, 0)  # First Row
        updated_arr = np.delete(updated_arr, len(
            updated_arr) - 1, 0)  # Last Row
        updated_arr = np.delete(updated_arr, 0, 1)  # First Column
        updated_arr = np.delete(updated_arr, len(
            updated_arr[0]) - 1, 1)  # Last Column
        return (updated_arr)


arr1 = np.ones((4, 5)) * np.arange(1, 6) - np.arange(4).reshape((4, 1))
print(strip_mat(arr1))
