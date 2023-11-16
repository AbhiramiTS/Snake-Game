import turtle
from turtle import Turtle, Screen
from snake import Snake  # Assuming you have a Snake class defined in 'snake.py'
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off automatic screen updates

# Create a snake object
snake = Snake()

# Set up key bindings for snake movement
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True  # Flag to control the game loop

while game_on:
    screen.update()  # Manually update the screen
    time.sleep(0.5)  # Introduce a delay to control the speed of the game
    snake.move()  # Move the snake

# Close the window when clicked
screen.exitonclick()
