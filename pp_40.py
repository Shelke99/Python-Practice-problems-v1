# Keep reading input until a sentinel value (e.g., -
import numpy as np

# from Python lists
a = np.array([1, 2, 3])          # 1D
b = np.array([[1,2,3],[4,5,6]])  # 2D

# utility constructors
zeros = np.zeros((3,4))
ones  = np.ones((2,2))
eye   = np.eye(3)                # identity matrix
ar    = np.arange(0, 10, 2)      # like range -> [0,2,4,6,8]
lin   = np.linspace(0,1,5)       # 5 evenly spaced values between 0 and 1
rand  = np.random.random((3,3))  # uniform random in [0,1)
# print(zeros)
print(ones)
print(eye)
print(ar)
print(lin)