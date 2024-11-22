from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("square")
        self.shapesize(1,6)
        self.goto(0,-350)

    def move_left(self):
        self.backward(20)

    def move_right(self):
        self.forward(20)
