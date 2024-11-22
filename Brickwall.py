from turtle import Turtle

class Brick(Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 5)
        self.color_type = color
        self.color(color)
        self.goto(x,y)