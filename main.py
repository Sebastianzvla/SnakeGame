from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

s_body = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(s_body.Up, "w")
screen.onkey(s_body.Down, "s")
screen.onkey(s_body.Right, "d")
screen.onkey(s_body.Left, "a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # 0.1s delay
    s_body.move()

    if s_body.Head.distance(food) < 15:
        food.refresh()
        s_body.extend()
        score.refresh_score()

    if s_body.Head.xcor() > 285 or s_body.Head.ycor() < -285 or s_body.Head.ycor() > 285 or s_body.Head.ycor() < -285:
        game_is_on = False
        score.game_over()

    for segment in s_body.seg[1:]:
        if s_body.Head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
