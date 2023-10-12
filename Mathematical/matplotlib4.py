import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['axes.unicode_minus'] = False

x = np.array(["数学成绩", "语文成绩", "英语成绩", "理综成绩"])
y = np.array([110 / 150 * 100, 120 / 150 * 100, 108 / 150 * 100, 190 / 300 * 100])

for a, b in zip(x, y):  # 柱子上的数字显示
    plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=7)

plt.bar(x, y, color='green', width=0.5)
# plt.barh(x, y)
plt.show()
