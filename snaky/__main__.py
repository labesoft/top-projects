"""The Snaky Game Application
-----------------------------

About this Module
------------------
This module is the main entry point of The Snaky Game Application.

"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-09"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

# Importing libraries
import random
import time
import turtle
from tkinter import TclError


def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


def game_over():
    time.sleep(1)
    screen.clear()
    screen.bgcolor('turquoise')
    scoring.goto(0, 0)
    scoring.write("GAME OVER", align="center", font=("Courier", 30, "bold"))
    scoring.write("Your Score is {}".format(score),
                  align="center", font=("Courier", 30, "bold"))
    time.sleep(2)
    exit()


def game_loop():
    global index, score, delay
    screen.update()
    # snake and fruit collisions
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("Score:{}".format(score), align="center",
                      font=("Courier", 24, "bold"))
        delay -= 0.001

        # Spawn Manager
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('square')
        new_fruit.color('red')
        new_fruit.penup()
        old_fruit.append(new_fruit)
    # adding ball to snake
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()

        old_fruit[index].goto(a, b)
    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)
    snake_move()
    ##snake and border collision
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or \
            snake.ycor() < -240:
        game_over()
    ## snake collision
    for food in old_fruit:
        if food.distance(snake) < 20:
            game_over()
    time.sleep(delay)


if __name__ == '__main__':
    """Main entry point of snaky"""
    # Creating a game screen
    screen = turtle.Screen()
    screen.title('labesoft SNAKE GAME')
    screen.setup(width=700, height=700)
    screen.tracer(0)
    turtle.bgcolor('turquoise')
    turtle.speed(5)
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(-310, 250)
    turtle.pendown()
    turtle.color('black')
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.penup()

    # Creating snake and food
    snake = turtle.Turtle()
    snake.speed(0)
    snake.shape('square')
    snake.color("black")
    snake.penup()
    snake.goto(0, 0)
    snake.direction = 'stop'
    fruit = turtle.Turtle()
    fruit.speed(0)
    fruit.shape('circle')
    fruit.color('red')
    fruit.penup()
    fruit.goto(30, 30)
    old_fruit = []
    scoring = turtle.Turtle()
    scoring.speed(0)
    scoring.color("black")
    scoring.penup()
    scoring.hideturtle()
    scoring.goto(0, 300)
    scoring.write("Score :", align="center", font=("Courier", 24, "bold"))

    # Keyboard binding
    screen.listen()
    screen.onkeypress(snake_go_up, "Up")
    screen.onkeypress(snake_go_down, "Down")
    screen.onkeypress(snake_go_left, "Left")
    screen.onkeypress(snake_go_right, "Right")

    # Game mainloop
    score = 0
    delay = 0.1
    while True:
        try:
            game_loop()
        except (turtle.Terminator, TclError):
            exit()

    # Add unit tests
