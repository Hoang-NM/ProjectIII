import numpy as np

x = np.array([[1, 2], [3, 4]])

print(np.sum(x))  # Compute sum of all element
print(np.sum(x, axis=0))  # Compute sum of each colume
print(np.sum(x, axis=1))  # Compute sum of each row
