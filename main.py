import turtle
import time, random
from Paddle import Paddle
from Ball import Ball
from Brickwall import Brick
from Scoreboard import Scoreboard

def construct_brickwall():
    y = 140
    for color in color_list:
        x = -550
        for i in range(11):
            brick = Brick(color, x, y)
            brick_list.append(brick)
            x += 110
        y += 30

def bounce_on_peripheral_walls():
    if ball.ycor() >= 380 and 120 <= ball.heading() <= 150: #bounce on top wall
        ball.setheading(random.randint(210,240))
        ball.hits += 1
    elif ball.ycor() >= 380 and 30 <= ball.heading() <= 60: #bounce on top wall
        ball.setheading(random.randint(300, 330))
        ball.hits += 1
    elif ball.xcor() >= 580 and 30 <= ball.heading() <= 60: #bounce on right wall
        ball.setheading(random.randint(120, 150))
        ball.hits += 1
    elif ball.xcor() >= 580 and 300 <= ball.heading() <= 330: #bounce on right wall
        ball.setheading(random.randint(210, 240))
        ball.hits += 1
    elif ball.xcor() <= -580 and 120 <= ball.heading() <= 150: #bounce on left wall
        ball.setheading(random.randint(30, 60))
        ball.hits += 1
    elif ball.xcor() <= -580 and 210 <= ball.heading() <= 240: #bounce on left wall
        ball.setheading(random.randint(300, 330))
        ball.hits += 1

def bounce_on_paddle():
    if -340 <= ball.ycor() <= -330 and abs(ball.xcor() - paddle.xcor()) <= 60: #bounce on paddle
        ball.hits += 1
        if 300 <= ball.heading() <= 330:
            ball.setheading(random.randint(30, 60))
        elif 210 <= ball.heading() <= 240:
            ball.setheading(random.randint(120, 150))

def bounce_on_bottom_wall():
    global paddle, ball
    if ball.ycor() <= -380: #bounce on bottom wall ---> LOSE
        scoreboard.clear()
        scoreboard.lives -= 1
        paddle.hideturtle()
        ball.hideturtle()
        del paddle, ball
        # Restart after life loss
        paddle = Paddle()
        ball = Ball()
        window.listen()
        window.onkeypress(paddle.move_left, "Left")
        window.onkeypress(paddle.move_right, "Right")

def bounce_on_brick_wall():
    for brick in brick_list[:]:
        if abs(ball.ycor() - brick.ycor()) <= 20 and abs(ball.xcor() - brick.xcor()) <= 50:
            ball.hits += 1
            scoreboard.clear()
            if brick.color_type == "yellow":
                scoreboard.score += 1
            if brick.color_type == "green":
                scoreboard.score += 3
            if brick.color_type == "orange":
                scoreboard.score += 5
                ball.moving_speed += 5
            if brick.color_type == "red":
                scoreboard.score += 7
                ball.moving_speed += 5
            brick.hideturtle()
            brick_list.remove(brick)
            if 120 <= ball.heading() <= 150:
                ball.setheading(random.randint(210,240))
            elif 30 <= ball.heading() <= 60:
                ball.setheading(random.randint(300, 330))
            elif 210 <= ball.heading() <= 240:
                ball.setheading(random.randint(120, 150))
            elif 300 <= ball.heading() <= 330:
                ball.setheading(random.randint(30, 60))
            break

brick_list = []
color_list = ["yellow", "green", "orange", "red"]

window = turtle.Screen()
window.title("Breakout Game")
window.setup(width=1200, height=800)
window.bgcolor("black")
window.tracer(0)

construct_brickwall()
scoreboard = Scoreboard()

paddle = Paddle()
ball = Ball()

window.listen()
window.onkeypress(paddle.move_left, "Left")
window.onkeypress(paddle.move_right, "Right")

while scoreboard.lives > 0:
    print(ball.moving_speed)
    if 4 <= ball.hits < 12:
        ball.moving_speed += 5
    elif 4 <= ball.hits < 12:
        ball.moving_speed += 5
    scoreboard.show_score()
    scoreboard.show_lives()
    window.update()
    ball.move()
    bounce_on_peripheral_walls() #check if
    bounce_on_paddle() #check if
    bounce_on_bottom_wall() #check if
    bounce_on_brick_wall() #check if

    time.sleep(0.05)

scoreboard.show_game_over()
window.mainloop()