import numpy as np

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
row = np.array([[0, 0], [3, 3]])
col = np.array([[0, 2], [0, 2]])
y = x[row, col]
z = x[x > 5]
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
b = np.array([1, 2 + 5j, 4, 3.5 + 7j])
i = np.arange(32).reshape((8, 4))

print(i[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])], end='\n\n')
print(b[np.iscomplex(b)])
print(b[~np.iscomplex(b)])
print(x, y, z, sep='\n\n')
print(a[~np.isnan(a)])
