from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

POINTS_TO_WIN = 5
INITIAL_SLEEP_VALUE = 0.1
sleep_time = INITIAL_SLEEP_VALUE

screen = Screen()
screen.bgcolor('black')
screen.title('My Pong')
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    # detect collision with upper/lower border
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if (ball.x_move > 0 and ball.distance(r_paddle) < 51 and ball.xcor() > 325) or \
       (ball.x_move < 0 and ball.distance(l_paddle) < 51 and ball.xcor() < -325):
        ball.bounce_x()

    # detect a miss
    if ball.xcor() > 380:
        ball.bounce_x()
        ball.home()
        scoreboard.l_point()
        sleep_time *= 0.9   # increase speed

    if ball.xcor() < -380:
        ball.bounce_x()
        ball.home()
        scoreboard.r_point()
        sleep_time *= 0.9   # increase speed

    # game over if one player reached 5 points
    if scoreboard.l_score >= POINTS_TO_WIN or scoreboard.r_score >= POINTS_TO_WIN:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
