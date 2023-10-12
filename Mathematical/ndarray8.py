import numpy as np

# a = np.array([1, 2, 3, 4])
# b = np.array([10, 20, 30, 40])
a = np.array([[1, 2, 3, 4],[5,6,7,8]])
b = np.array([10,20,30,40])
if a.shape == b.shape:
    c = a * b
else:
    c = a + b

print(c)
