from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.lives = 3

    def show_score(self):
        self.goto(420, 320)
        self.write(f"Score: {self.score}", font=("Helvetica", 25, "normal"))

    def show_lives(self):
        self.goto(-570, 320)
        self.write(f"Lives: {self.lives}", font=("Helvetica", 25, "normal"))

    def show_game_over(self):
        self.goto(-100, 0)
        self.write(f"Game Over\nYour Score: {self.score}", font=("Helvetica", 35, "bold"))