from turtle import Turtle


class Scoreboard(Turtle):
    """
    Controls the scoring system
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.refresh()

    def refresh(self):
        """
        Updates the score with the new points
        :return:
        """
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", True, "center", ("rockwell", 12, "normal"))

    def score_gained(self):
        """
        Adds 1 point to the score
        :return:
        """
        self.score += 1
        self.refresh()

    def game_over(self):
        """
        Declares game over and shows the total score in points
        :return:
        """
        self.goto(0,0)
        self.write(f"Game Over! Your Score: {self.score}", True, "center", ("rockwell", 24, "normal"))
