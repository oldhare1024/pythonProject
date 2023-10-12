import numpy as np

a = np.arange(10)
s = slice(2, 8, 2)
t = a[2:8:2]
u = a[5]
b = np.array([[1, 2, 3], [5, 2, 6], [5, 4, 7]])
v = np.array([[1, 2], [3, 4], [5, 6]])
w = v[[0, 1, 2], [0, 1, 0]]

print(a[s], t)
print(a[2:])
print(b[1:])
print(b[..., 1], b[1, ...], b[..., 1:], sep='\n')
print(w)
print(u)
