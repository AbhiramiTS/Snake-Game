import turtle
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off automatic screen updates

# Create a snake object
snake = Snake()

# Create a food object
food = Food()

# Create a ScoreBoard object to keep track of the score
score_board = ScoreBoard()

# Set up key bindings for snake movement
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True  # Flag to control the game loop

while game_on:
    screen.update()  # Manually update the screen
    time.sleep(0.1)  # Introduce a delay to control the speed of the game
    snake.move()  # Move the snake

    # Check if the snake has eaten the food
    if snake.head.distance(food) < 15:
        score_board.increment_score()  # Increase the score
        food.refresh()  # Move the food to a new random location
        snake.extend_segment()  # Extend the snake by adding a new segment

    # Detect collision with the wall
    if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
    ):
        game_on = False  # End the game if the snake hits the wall

    # Detect collision with the snake's tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False  # End the game if the snake collides with its tail

# Display the game over message on the scoreboard
score_board.game_over()

# Close the window when clicked
screen.exitonclick()
