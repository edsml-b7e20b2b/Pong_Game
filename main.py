from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

sc = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len= 1)
# paddle.penup()
#
# paddle.setpos(350, 0)
#
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y )
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y )


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

#      detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#   detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() >340) or (ball.distance(left_paddle) < 50 and  ball.xcor() <-340):
        ball.bounce_x()


    if ball.xcor()> 380 :
        ball.reset_game()
        sc.l_point()

    if -380> ball.xcor():
        ball.reset_game()
        sc.r_point()
















screen.exitonclick()
