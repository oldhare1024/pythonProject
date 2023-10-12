import matplotlib4.pyplot as plt
import numpy as np
import matplotlib4

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['axes.unicode_minus']=False
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 50])
# plt.plot(xpoints, ypoints)
# plt.plot(xpoints, ypoints,'o')
# x1points = np.array([1, 2, 6, 8])
# y1points = np.array([3, 8])
# plt.plot(x1points, y1points)
# plt.plot(y1points)
x = np.arange(0, 2 * np.pi, 0.1)
y = np.sin(x)
# z=np.cos(x)
plt.plot(x, y, 'o--r', markevery=15, ms=10, mfc='b', mec='c', linewidth='5')
plt.title("rabb1t test")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.grid(visible=True)
plt.show()
