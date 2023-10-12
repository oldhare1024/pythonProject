import numpy as np

a = np.arange(1, 10, dtype=float).reshape(3, 3)
b = np.array([1, 2, 3])

print('矩阵\n{}\n 与 矩阵\n{}\n相加为\n{}\n'.format(a, b, np.add(a, b)))
print('矩阵\n{}\n 与 矩阵\n{}\n相减为\n{}\n'.format(a, b, np.subtract(a, b)))
print('矩阵\n{}\n 与 矩阵\n{}\n相乘为\n{}\n'.format(a, b, np.multiply(a, b)))
print('矩阵\n{}\n 与 矩阵\n{}\n相除为\n{}\n'.format(a, b, np.divide(a, b)))

print('{}的倒数矩阵为\n{}'.format(a, np.reciprocal(a)))
print('{}的平方为\n{}'.format(a, np.power(a, 2)))
print('{}对应b的幂值为\n{}'.format(a, np.power(a, b)))
print('{}对{}取余为\n{}'.format(a, b, np.mod(a, b)))
