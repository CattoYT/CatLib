import random as r
import turtle as t

class catLib:
    def __init__(self, turtle):
        self.t = turtle

    def drawSquare(self, size):
        for _ in range(4):
            self.t.forward(size)
            self.t.right(90)

    def drawRect(self, width, height, color=None):
        self.t.begin_fill()
        if color is None:
            self.t.color("black")
        else:
            self.t.color(color)
        self.t.setheading(90)
        for _ in range(2):
            self.t.forward(height)
            self.t.right(90)
            self.t.forward(width)
            self.t.right(90)
        self.t.end_fill()

    def drawTriangle(self, size, filled, color):
        if filled:
            previousColor = self.t.pencolor()
            self.t.color(color)
            self.t.begin_fill()
        for _ in range(3):
            self.t.forward(size)
            self.t.right(120)
        if filled:
            self.t.end_fill()
            self.t.color(previousColor)
            del(previousColor)

    def drawCircle(self, size):
        self.t.circle(size)

    def drawCustom(self, sides, size, angle, color):
        self.t.color(color)
        for _ in range(sides):
            self.t.forward(size)
            self.t.right(angle)

    def drawRandom(self, size):
        temp = 60
        print(temp)
        for _ in range(temp):
            self.t.forward(size)
            self.t.right(((temp - 2) * 360) / temp)

    def draw5PointStar(self, color):
        self.t.color(color)
        self.t.begin_fill()
        for _ in range(5):
            self.t.forward(100)
            self.t.right(144)
        self.t.end_fill()

    def draw2LayeredFlag(self, color1, color2):
        self.drawRect(50, 200, color1)
        self.t.setheading(270)
        self.t.forward(50)
        self.drawRect(50, 200, color2)

    def draw3LayeredVerticalFlag(self, color1, color2, color3, borderStatus):
        self.drawRect(50, 150, color1)
        self.t.setheading(0)
        self.t.forward(50)
        self.t.left(90)
        self.drawRect(50, 150, color2)
        self.t.setheading(0)
        self.t.forward(50)
        self.t.left(90)
        self.drawRect(50, 150, color3)
        if borderStatus:
            self.t.setheading(0)
            self.t.forward(50)
            self.t.setheading(180)
            self.t.color("black")
            for _ in range(2):
                self.t.forward(150)
                self.t.right(90)

    def drawFlag(self, country):
        if country == "somalia":
            self.drawRect(300, 150, "cyan")
            self.t.setheading(90)
            self.t.forward(100)
            self.t.setheading(0)
            self.t.forward(100)
            self.draw5PointStar("white")
        elif country == "vietnam":
            self.drawRect(300, 150, "red")
            self.t.setheading(90)
            self.t.forward(100)
            self.t.setheading(0)
            self.t.forward(100)
            self.draw5PointStar("yellow")
