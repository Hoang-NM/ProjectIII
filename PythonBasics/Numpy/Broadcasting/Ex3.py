import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])

y = x + v  # Add v to each row of x using Broadcasting, storing in vector y
print(y)
