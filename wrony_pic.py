from turtle import *  # 导入海龟绘图库


# 定义绘制线段函数，参数为起始、终止点坐标
def line(x1, y1, x2, y2):
    penup()  # 抬笔
    goto(x1, y1)  # 移动到线段起点
    pendown()  # 落笔
    goto(x2, y2)  # 移动到线段终点


speed(10)  # 加速绘制
# 画出多条黑色斜线
for x in range(-600, 600, 63):
    line(0, 200, x, 0)  # 上面的斜线
    line(0, -200, x, 0)  # 下面的斜线
# 画出两条红色平行线
color('red')
line(-600, 100, 600, 100)
line(-600, -100, 600, -100)
# 隐藏笔形状、绘制结束
hideturtle()
mainloop()
