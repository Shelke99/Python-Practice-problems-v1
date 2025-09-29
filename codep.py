import numpy as np

# Create array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Element-wise operations
print("Array + 10:", arr + 10)
print("Array squared:", arr ** 2)

# Multi-dimensional array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("Matrix:\n", matrix)

# Matrix multiplication
result = np.dot(matrix, [[1], [2], [3]])
print("Matrix multiplication result:\n", result)

# Random numbers
rand_nums = np.random.rand(5)
print("Random Numbers:", rand_nums)
