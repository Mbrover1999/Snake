import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.update()
screen.listen()
game_is_on = True
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")


while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.05)
    if snake.head.distance(food) < 15:
        print("nom nom")
        food.refresh()
        scoreboard.addScore()
        snake.extend()
        screen.update()
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()
        food.refresh()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            food.refresh()

screen.exitonclick()
