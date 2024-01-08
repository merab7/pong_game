from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=3, stretch_len=0.8)
        self.penup()
        self.goto(pos)

    def move_up(self):
        if self.pos()[1] < 250:
            self.goto(self.pos()[0], self.pos()[1] + 50)

    def move_down(self):
        if self.pos()[1] > -250:
            self.goto(self.pos()[0], self.pos()[1] - 50)
