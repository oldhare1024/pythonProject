import random as r
import turtle as t

print(r.randint(0, 255))
a = t.numinput(' 请输入', '画笔粗细')
t.pensize(a)
t.hideturtle()
b = int(t.textinput('速度', '绘图速度'))
t.speed(b)
t.fillcolor('orange')
t.begin_fill()
t.pencolor('red');
t.fd(50);
t.right(90)
t.pencolor('red');
t.fd(50);
t.left(90)
t.pencolor('red');
t.fd(50);
t.left(90)
t.pencolor('red');
t.fd(50);
t.right(90)
t.pencolor('red');
t.fd(50);
t.right(90)
t.pencolor('green');
t.fd(100);
t.right(90)
t.pencolor('#F01');
t.fd(150);
t.right(90)
t.pencolor('green');
t.fd(100)
t.end_fill()
t.mainloop()
