from sklearn.datasets import load_digits
from random import randint
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
# %config InlineBackend.figure_format = 'svg'
plt.style.use('ggplot')


def perceptron_train(X, Y, iterations=100, eta=.1):
    '''
    Trains a perceptron and returns the weights and learning curve as a vector of accuracies.

    Input:
    - X: Pixel matrix to encode the digits (every row is a gray-valued pixel vector for a number)
    - Y: Vector of true labels i.e. Y[0] is the label for the first digit in the dataset
    - iterations: Maximum number of allowed iterations. Defaults to 100.
    - eta: Learning rate for SGD. Defaults to 0.1.

    Output:
    - weights: The parameters of the linear decision boundary.
    - acc: Vector of accuracies for every iteration step.
    '''

    acc = np.zeros(iterations)
    # Initialize weight vector
    D = len(X[0])  # Dimension of each sample matrix
    N = len(Y)  # Number of samples equal to number of result
    weights = np.array([1/D] * D)
    for it in range(0, iterations):
        for j in range(N):
            i = randint(0, N-1)
            result = np.matmul(weights.T, X[i])
            if np.sign(result) != Y[i]:
                weights = weights + (eta/(it+1)) * (X[i]*Y[i])
                break

        # Calculate accuracy
        correct_count = 0
        for j in range(N):
            result = np.matmul(weights.T, X[j])
            if np.sign(result) == Y[j]:
                correct_count += 1
        acc[it] = correct_count / N

    # Return weight vector and accuracy
    return weights, acc


# The following code is for testing purposes
# Your plots may differ slightly, but they should always converge towards a high accuracy very fast.

digit_to_recognize = 3  # You can pick any other one from 0 to 9

# Load the usps digits dataset from sklearn repository
X, Y = load_digits(n_class=10, return_X_y=True)

# Plot one example of the chosen digit
for i in range(len(X)):
    if Y[i] == digit_to_recognize:
        plt.matshow(X[i, :].reshape(8, 8))
        plt.xticks([])
        plt.yticks([])
        plt.title(Y[i])
        plt.savefig("usps_example.png")
        break

# Transform the 10-class labels into binary form
y = np.sign((Y == digit_to_recognize) * 1.0 - .5)
_, acc = perceptron_train(X, y)
plt.figure(figsize=[12, 4])
plt.plot(acc)
plt.xlabel("Iterations")
plt.ylabel("Accuracy")
plt.savefig("learning_curve.png")
plt.show()
