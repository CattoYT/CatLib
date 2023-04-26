import random as r
import turtle as t

def drawSquare(size):
    
    for i in range(4):
        t.forward(size)
        t.right(90)


def drawRect(width, height, color):
    t.begin_fill()
    if color == None:
        t.color("black")
    else:
        t.color(color)
    t.setheading(90)
    for i in range(2):
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()

def drawTriangle(size, filled, color):
    if filled:
        previousColor = t.pencolor()
        t.color(color)
        t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.right(120)
    if filled:
        t.end_fill()
        t.color(previousColor)
        del(previousColor)

def drawCircle(size):
    t.circle(size)

def drawCustom(sides, size, angle, color):
    t.color(color)
    for i in range(sides):
        t.forward(size)
        t.right(angle)

def drawRandom(size):

    temp = 60
    print(temp)
    for i in range(temp):
        t.forward(size)
        t.right(((temp-2)*360)/temp)


#29/3/23 additions

def draw5PointStar(color):
    t.color(color)
    t.begin_fill()
    for i in range(5):

       t.forward(100)

       t.right(144)
    t.end_fill()
def draw2LayeredFlag(color1, color2):
    drawRect(50, 200, color1)
    t.setheading(270)
    t.forward(50)
    drawRect(50, 200, color2)

def draw3LayeredVerticalFlag(color1, color2, color3, borderStatus):
    drawRect(50, 150, color1)
    t.setheading(0)
    t.forward(50)
    t.left(90)
    drawRect(50, 150, color2)
    t.setheading(0)
    t.forward(50)
    t.left(90)
    drawRect(50, 150, color3)
    if borderStatus:
        t.setheading(0)
        t.forward(50)
        t.setheading(180)
        t.color("black")
        for i in range(2):
            t.forward(150)
            t.right(90)
            t.forward(150)
            t.right(90)



def drawFlag(country):
    
    if country == "somalia":
        drawRect(300, 150, "cyan")


        t.setheading(90)
        t.forward(100)
        t.setheading(0)
        t.forward(100)
        draw5PointStar("white")
    if country == "vietnam":
        drawRect(300, 150, "red")


        t.setheading(90)
        t.forward(100)
        t.setheading(0)
        t.forward(100)
        draw5PointStar("yellow")


    
