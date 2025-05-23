# Create the Screen
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


WIDTH = 800
HEIGHT = 600
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=WIDTH,height=HEIGHT)
screen.tracer(0)



l_paddle = Paddle((-360,0))
r_paddle = Paddle((350,0))
score = Score()
screen.listen()

screen.onkeypress(fun=r_paddle.go_up,key="Up")
screen.onkeypress(fun=r_paddle.go_down,key="Down")

screen.onkeypress(fun=l_paddle.go_up,key="w")
screen.onkeypress(fun=l_paddle.go_down,key="s")

ball = Ball()
game_is_on = True


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.go_up()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with one of the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.refresh()
        score.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.refresh()
        score.r_point()

screen.exitonclick()