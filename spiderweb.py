
import turtle as t
t.speed(2)
t.bgcolor("Black")
t.pencolor("Red")
for i in range(6):
    t.forward(150)
    t.backward(150)
    t.right(60)
side=50
t.fillcolor("green")
t.begin_fill()
for i in range(15):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.setheading(0)
    t.forward(side)
    t.right(120)
    for j in range(6):
        t.forward(side-2)
        t.right(60)
    side=side-10
t.end_fill()
turtle.done()