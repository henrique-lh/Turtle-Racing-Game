import random
import turtle

from games.space_invaders.constants import ALIEN_SPEED


class Alien:
    def __init__(self, x, y):
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.turtlesize(1.5)
        self.t.setposition(x, y)
        self.t.shape("turtle")
        self.t.setheading(-90)
        self.t.color(random.random(), random.random(), random.random())

    def move(self):
        self.t.forward(ALIEN_SPEED)

    def cleanup(self):
        self.t.clear()
        self.t.hideturtle()

    def get_y(self):
        return self.t.ycor()

    def get_pos(self):
        return self.t.pos()