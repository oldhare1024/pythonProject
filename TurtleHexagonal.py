import turtle

t = turtle.Turtle()
t.pencolor(1, 0, 0)
t.pensize(3)

for i in range(6):
    t.forward(50)
    t.right(60)

t.right(120)
t.forward(50)
t.left(60)
t.forward(50)
t.left(60)
t.forward(50)

for i in range(5):
    t.right(60)
    t.forward(50)

t.right(60)

turtle.done()
