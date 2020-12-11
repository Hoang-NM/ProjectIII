import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = a[:2, 1:3]

print(a[0, 1])
b[0, 0] = 76
print(a[0, 1])

row_r1 = a[1, :]  # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)

col_r1 = a[:, 1]  # Rank 1 view of the second col of a
col_r2 = a[:, 1:2]  # Rank 2 view of the second col of a
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)
