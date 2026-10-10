import numpy as np

# 1. Create arrays
arr = np.array([10, 20, 30, 40, 50])
matrix = np.array([[1, 2], [3, 4]])

# 2. Perform operations
print("Sum:", np.sum(arr))
print("Matrix Multiplication:\n", np.dot(matrix, matrix))

# 3. Random sampling (without replacement)
samples = np.random.choice(arr, size=3, replace=False)
print("Random Samples:", samples)   