import numpy as np

v = np.array([1, 2, 3])
w = np.array([4, 5])

print(np.reshape(v, (3, 1)) * w)

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x + v)  # x has shape (3, 2) and v has shape (3,) so they broadcast to (3, 2)

print((x.T + w).T)

print(x + np.reshape(w, (2, 1)))

print(x * 2)  # Multiply a matrix
