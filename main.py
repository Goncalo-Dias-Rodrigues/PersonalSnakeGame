from turtle import Screen, Turtle

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_over = False
while not game_over:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 30:
        food.refresh()
        scoreboard.score_gained()
        snake.extend()

    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        game_over = True
        scoreboard.game_over()

    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
