import numpy as np

rand_arr = np.random.randint(1, 10, size=(3,3))
print("Random Array:\n", rand_arr)


arr2D = np.array([[1, 2, 3], [4, 5, 6]])
arr1D = np.array([10, 20, 30])

print("Broadcasted:\n", arr2D + arr1D)
