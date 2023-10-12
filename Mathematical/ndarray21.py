import numpy as np

a = np.arange(4).reshape(2, 2)
b = np.arange(6).reshape(2, 3)

print(a, b, sep='\n')
print(np.dot(a, b))

c = np.array([[1, 2], [3, 4]])
d = np.array([[11, 12], [13, 14]])

print(np.vdot(c, d))

e = np.array([1, 2, 3])
f = np.array([0, 1, 0])

print(np.inner(e, f))

g = np.array([[1, 2, 4], [3, 4, 5], [7, 8, 10]])

print(g, np.linalg.det(g), sep='\n')

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.linalg.inv(x)
print(x, y, np.dot(x, y), sep='\n')

h = np.array([[1, 2], [3, 5]])
i = np.array([[1], [2]])
g = np.linalg.solve(h, i)
print(h, i, g, sep='\n')
