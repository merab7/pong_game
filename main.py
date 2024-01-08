from turtle import Screen
import sys
import random
from paddle import Paddle
from ball import Ball
import time
from score_board import Board

pl1_score = 0
pl2_score = 0
game_on = True


def play():
    global pl1_score, pl2_score, game_on
    game_on = True
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.bgcolor("black")
    screen.tracer(0)
    r_paddle = Paddle((370, 0))
    l_paddle = Paddle((-370, 0))
    ball = Ball()
    pl_1_board = Board((200, -280), score=pl1_score)

    pl_2_board = Board((-200, -280), score=pl2_score)

    screen.listen()
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")

    while game_on:
        screen.update()
        time.sleep(ball.sleep_time)
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
        elif ball.xcor() > 390 or ball.xcor() < -390:
            if ball.xcor() > 390:
                pl2_score += 1
                pl_2_board.add(pl2_score)
            elif ball.xcor() < -390:
                pl1_score += 1
                pl_1_board.add(pl1_score)

            ball.reset()


play()

screen.exitonclick()
