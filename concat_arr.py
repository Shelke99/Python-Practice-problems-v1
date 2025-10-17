import numpy as np
from numpy.random._examples.cffi.extending import rng

arr1 = np.array([[1,2,3],[12,4,5]])
arr2 = np.array([[6,7,8],[9,10,11]])
# print(np.concatenate([arr1, arr2]))
sample = np.concatenate([arr1, arr2])
s1 = np.vstack((arr1, arr2))                    #np.vstack([arr1, arr2])
s2 = np.hstack([arr1,arr2])

print(s1)
print(s2)
# arr = np. array([[ 1,  2,  3],
#                  [ 4,  5,  6],
#                   [ 7,  8,  9],
#                   [10, 11, 12]])
arr3 = rng.standard_normal((5, 2))
print(arr3)
