from turtle import Turtle

# Constants
ALIGN = "center"
FONT = ("Arial", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        """
        Initialize the ScoreBoard object.
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        """
        Update and display the current score.
        """
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increment_score(self):
        """
        Increment the score, clear the previous score, and update the display.
        """
        self.score += 1
        self.clear()
        self.update_score()
