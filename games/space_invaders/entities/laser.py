import turtle

from games.space_invaders.constants import LASER_SPEED, LASER_LENGTH


class Laser:
    def __init__(self, x, y):
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.color(1, 0, 0)
        self.t.hideturtle()
        self.t.setposition(x, y)
        self.t.setheading(90)
        self.t.forward(20)
        self.t.pendown()
        self.t.pensize(5)

    def move(self):
        self.t.clear()
        self.t.forward(LASER_SPEED)
        self.t.forward(LASER_LENGTH)
        self.t.forward(-LASER_LENGTH)

    def cleanup(self):
        self.t.clear()
        self.t.hideturtle()

    def get_y(self):
        return self.t.ycor()

    def get_pos(self):
        return self.t.pos()
