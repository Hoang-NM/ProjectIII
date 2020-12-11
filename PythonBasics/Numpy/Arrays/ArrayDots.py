import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

# Inner product of vectors
print(v.dot(w))
print(np.dot(v, w))

# Matrix/Vector product - rank 1 array
print(x.dot(v))
print(np.dot(x, v))

# Matrix/Vector product - rank 2 array
print(x.dot(y))
print(np.dot(x, y))
