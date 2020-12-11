import numpy as np

x = np.array([[1, 2], [3, 4]])
print(x)
print(x.T)  # Transpose a matrix

# Transpose of a rank 1 array does nothing
v = np.array([1, 2, 3])
print(v)
print(v.T)
