import numpy as np

a = np.arange(6).reshape(2, 3)
print('原始数组是:\n{}'.format(a))
print('迭代输出元素:')
for x in np.nditer(a):
    print(x, end=",")
print('\n')
print('转置矩阵为:')
print(a.T)
for x in np.nditer(a, order='F'):
    print(x, end=",")
print('\n')
for x in np.nditer(a, order='C'):
    print(x, end=",")
print('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print(a)

b = np.arange(0, 60, 5).reshape(3, 4)
print('原始数组是：')
print(b)
print('\n')
print('修改后的数组是：')
for x in np.nditer(b, flags=['multi_index'], order='F'):
    print(x, end=", ")
print('\n')
c = np.arange(0, 60, 5)
c = c.reshape(3, 4)
print('第一个数组为：')
print(c)
print('\n')
print('第二个数组为：')
d = np.array([1, 2, 3, 4], dtype=int)
print(d)
print('\n')
print('修改后的数组为：')
for x, y in np.nditer([c, d]):
    print("%d:%d" % (x, y), end=", ")
