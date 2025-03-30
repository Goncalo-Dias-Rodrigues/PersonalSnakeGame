from turtle import Turtle
import random

class Food(Turtle):
    """
    Normal Snake food. When the snake catches one food, the food relocates to a random part of the screen
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.color("green")
        self.refresh()

    def refresh(self):
        """
        the food relocates to a random part of the screen
        :return:
        """
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
