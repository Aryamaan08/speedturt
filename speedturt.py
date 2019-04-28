import turtle

t = turtle.Turtle()
def circle(size=1):
    for i in range(0, 360):
        t.forward(size)
        t.right(size)
def semi_circle(size=1):
    for i in range(0, 180):
        t.forward(size)
        t.right(size)
def square(size=100):
    for i in range(0, 4):
        t.forward(size)
        t.right(90)
def triangle(size=100):
    for i in range(0, 3):
        t.forward(size)
        t.right(120)
def pentagon(size=50):
    for i in range(0, 5):
        t.forward(size)
        t.right(72)
def turtle_shape():
    t.shape('turtle')
def circle_shape():
    t.shape('circle')
def square_shape():
    t.shape('square')
def triangle_shape():
    t.shape('triangle')
def arrow_shape():
    t.shape('arrow')
def bg(hex):
    turtle.Screen().bgcol(hex)
def tc(hex):
    t.color(hex)
def tpc(hex):
    t.pencolor(hex)
def tps(size=5):
    t.pensize(size)