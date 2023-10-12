import numpy as np

a = np.array([0, 30, 45, 60, 90])
s = np.sin(a * np.pi / 180)
c = np.cos(a * np.pi / 180)
t = np.tan(a * np.pi / 180)

print('各角度的sin值为:{}'.format(s))  # 将角度转换为弧度计算
print('各角度的cos值为:{}'.format(c))
print('各角度的tan值为:{}'.format(t))

arcs = np.arcsin(s)
arcc = np.arccos(c)
arct = np.arctan(t)

print('各正三角函数值的反三角函数弧度为')
print(arcs, arcc, arct, sep='\n')

b = [0.4, 0.5, 0.6, -0.4, -0.5, -0.6]
c = [1.4, 1.5, 1.6, -1.4, -1.5, -1.6]
d = [2.4, 2.5, 2.6, -2.4, -2.5, -2.6]
e = [3.4, 3.5, 3.6, -3.4, -3.5, -3.6]

print(np.around(b))
print(np.around(c))
print(np.around(d))
print(np.around(e))
print(f'{4.56:.20f}')
print(round(1.25,1))
print(f'{7.56:.20f}')
print(round(7.75,1))
print(np.floor(b))
print(np.ceil(c))
