import numpy as np

a, b = 13, 17
print('{}和{}的二进制为{},{}'.format(a, b, bin(a), bin(b)))
print('{}和{}的位与结果为{}'.format(a, b, np.bitwise_and(a, b)))
print('{}和{}的位或结果为{}'.format(a, b, np.bitwise_or(a, b)))
c = 25
print('{}取反为{}'.format(c, np.invert(c, dtype=np.uint8)))
d, e = 10, 40
print('将{}左移两位为{}'.format(d, np.left_shift(d, 2)))
print('将{}右移两位为{}'.format(e, np.right_shift(e, 2)))
print('{}的二进制为{}'.format(d, np.binary_repr(d, width=8)))
print('{}的二进制为{}'.format(e, np.binary_repr(e, width=8)))
