import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['axes.unicode_minus'] = False

y = np.array([35, 25, 25, 15])
explode = (0, 0.1, 0, 0)
plt.pie(y,
        labels=['A', 'B', 'C', 'D'],
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"],
        explode=explode,
        shadow=True,
        startangle=90,
        autopct='%.2f%%',
        )
plt.title("RUNOOB Pie Test")  # 设置标题
plt.show()
