from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        # Initialize the snake with starting positions
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        # Create the initial snake with three segments
        for position in STARTING_POSITIONS:
            snake = Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snake_segments.append(snake)

    def move(self):
        # Move the snake forward
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            x_index = self.snake_segments[seg_num - 1].xcor()
            y_index = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(x_index, y_index)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        # Turn the snake left if it's not already moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Turn the snake right if it's not already moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        # Turn the snake up if it's not already moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Turn the snake down if it's not already moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
