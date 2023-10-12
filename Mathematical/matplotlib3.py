import matplotlib4.pyplot as plt
import numpy as np
import matplotlib4

np.random.seed(20230911)
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['axes.unicode_minus']=False
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
# sizes=np.array([20,50,100,200,500,1000,60,90])
# colors=np.array(["red","green","black","orange","purple","beige","cyan","magenta"])
N=11
x = np.random.rand(N)
y = np.random.rand(N)
colors=np.random.rand(N)
area=(30*np.random.rand(N))**2
colors2=np.array([0,10,20,30,40,50,60,70,80,90,100])
plt.scatter(x, y,s=area,c=colors2,alpha=0.5)
plt.title("二十次随机散点图")
plt.show()
