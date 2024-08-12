import numpy as np
import matplotlib.pyplot as plt

# Generate random data points for two classes
np.random.seed(0)
class1_points = np.random.randn(50, 2) + np.array([1, 1])
class2_points = np.random.randn(50, 2) + np.array([-1, -1])

# Concatenate the data points and add bias term
X = np.vstack([class1_points, class2_points])
X = np.hstack([np.ones((X.shape[0], 1)), X])  # Add bias term

# Define target labels (0 for class 1, 1 for class 2)
Y = np.hstack([np.zeros(50), np.ones(50)])

# Initialize weight vector randomly
weights = np.random.randn(X.shape[1])

# Learning rate
learning_rate = 0.01

# Number of epochs
epochs = 1000

# LMS algorithm for binary classification
for _ in range(epochs):
    for i in range(X.shape[0]):
        x_i = X[i]
        y_i = Y[i]
        prediction = np.dot(weights, x_i)
        error = y_i - prediction
        weights += learning_rate * error * x_i

# Plotting the decision boundary
x_vals = np.linspace(-4, 4, 100)
y_vals = -(weights[0] + weights[1] * x_vals) / weights[2]

plt.figure(figsize=(8, 6))
plt.scatter(class1_points[:, 0], class1_points[:, 1], label='Class 1')
plt.scatter(class2_points[:, 0], class2_points[:, 1], label='Class 2')
plt.plot(x_vals, y_vals, color='red', label='Decision Boundary')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Binary Classification with LMS')
plt.legend()
plt.grid(True)
plt.show()
