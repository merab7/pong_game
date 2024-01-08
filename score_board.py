from turtle import Turtle


class Board(Turtle):
    def __init__(self, pos, score):
        super().__init__()
        self.score = score
        self.color("White")
        self.penup()
        self.goto(pos)
        self.pendown()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 12, 'normal'))
        self.hideturtle()

    def add(self, score):
        self.clear()
        self.write(f"Score: {score}", move=False, align='center', font=('Arial', 12, 'normal'))

    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 100)
    #     self.pendown()
    #     self.color("red")
    #     self.write(f"Game over.", move=False, align='center', font=('Arial', 12, 'bold'))
