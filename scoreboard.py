from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", True, "center", ("rockwell", 12, "normal"))

    def score_gained(self):
        self.score += 1
        self.refresh()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over! Your Score: {self.score}", True, "center", ("rockwell", 24, "normal"))
