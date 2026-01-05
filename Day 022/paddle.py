from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)
        self.moving_up = False
        self.moving_down = False

    def go_up_start(self):
        self.moving_up = True

    def go_up_stop(self):
        self.moving_up = False

    def go_down_start(self):
        self.moving_down = True

    def go_down_stop(self):
        self.moving_down = False

    def move(self):
        if self.moving_up:
            self.sety(self.ycor() + 20)
        if self.moving_down:
            self.sety(self.ycor() - 20)
