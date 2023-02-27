import turtle
x=turtle.Screen()
x.setup(width=400,height=400)
y=turtle.Turtle()
def curve():
    for i in range(200):
        y.right(1)
        y.forward(1)
def heart():
    y.fillcolor('red')
    y.begin_fill()
    y.left(140)
    y.forward(113)
    curve()
    y.left(120)
    curve()
    y.forward(112)
    y.goto(-30,65)
    y.write("ℍ𝕖 𝔸𝕣𝕥 𝕓𝕪 𝕔𝕙𝕒𝕟𝕕𝕦")
    y.end_fill()
    
heart()
y.ht()
turtle.done()
    