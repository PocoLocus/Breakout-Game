from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(1)
        self.goto(0,-329)
        self.setheading(random.randint(30,60))
        self.moving_speed = 15
        self.hits = 0

    def move(self):
        self.forward(self.moving_speed)


