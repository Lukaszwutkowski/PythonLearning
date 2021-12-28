from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

player_1 = Player((350, 0))
player_2 = Player((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_1.go_up, "Up")
screen.onkey(player_1.go_down, "Down")
screen.onkey(player_2.go_up, "w")
screen.onkey(player_2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with players
    if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right side misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.p_1_score()

    # Detect when left side misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.p_2_score()

screen.exitonclick()
