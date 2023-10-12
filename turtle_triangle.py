import turtle

t = turtle.Turtle()

t.penup()
t.goto(-120, 0)
t.pendown()

for i in range(3):
    t.fd(240)
    t.left(120)
t.fd(120)
# t.left(120)
t.seth(120)
t.fd(120)
# t.left(240)
t.seth(0)
t.fd(120)
# t.left(240)
t.seth(240)
t.fd(120)
turtle.done()
