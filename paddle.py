from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.x_move = 40
        self.y_move = 40

    def go_up(self):
        new_y = self.ycor() + self.x_move
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - self.y_move
        self.goto(self.xcor(), new_y)
