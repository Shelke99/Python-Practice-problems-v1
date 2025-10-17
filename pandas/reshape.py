import numpy as np

arr = np.arange(1, 17)   # [1, 2, ..., 12]
print("Original:", arr)

reshaped = arr.reshape(4, 4)
print("Reshaped 3x4:\n", reshaped)

flattened = reshaped.flatten()
print("Flattened:", flattened)
