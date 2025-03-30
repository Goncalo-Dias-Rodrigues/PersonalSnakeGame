from turtle import Turtle

DISTANCE_FROM_SQUARES = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    The snake itself. The head gets directions and the rest of the squares that are part of the snake follow it
    """

    squares = []

    def __init__(self):
        spawn_x = 0
        for i in range(3):
            new_turtle = self.add_square()
            new_turtle.goto(spawn_x, 0)
            self.squares.append(new_turtle)
            spawn_x -= DISTANCE_FROM_SQUARES
        self.head = self.squares[0]

    def move(self):
        """
        Function to move the body of the snake by moving each square to the location of the square after it
        :return:
        """
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.head.forward(DISTANCE_FROM_SQUARES)

    def extend(self):
        """
        Adds 1 more square to the body of the snake
        :return:
        """
        new_turtle = self.add_square()
        new_turtle.goto(self.squares[-1].xcor(), self.squares[-1].ycor())
        self.squares.append(new_turtle)

    def add_square(self):
        """
        Creates the square that is going to be added
        :return: body square
        """
        new_turtle = Turtle()
        new_turtle.color("red")
        new_turtle.shape("square")
        new_turtle.penup()
        return new_turtle

    def up(self):
        """
        Rotates the snake head upwards
        :return:
        """
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Rotates the snake head upwards
        :return:
        """
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Rotates the snake head left
        :return:
        """
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Rotates the snake head right
        :return:
        """
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
