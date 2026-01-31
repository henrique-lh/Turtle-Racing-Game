import turtle

from games.space_invaders.constants import CANNON_STEP


class Cannon:
    def __init__(self, x, y, floor_level):
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.color(1, 1, 1)
        self.t.shape("square")
        self.t.setposition(x, y)
        self.floor_level = floor_level
        self.movement_dir = 0  # -1, 0, 1

    def change_direction(self, direction):
        self.movement_dir = direction

    def update_position(self, left_bound, right_bound):
        new_x = self.t.xcor() + CANNON_STEP * self.movement_dir
        if left_bound <= new_x <= right_bound:
            self.t.setx(new_x)
        self.draw()

    def draw(self):
        self.t.clear()
        self.t.turtlesize(1, 4)  # Base
        self.t.stamp()
        self.t.sety(self.floor_level + 10)
        self.t.turtlesize(1, 1.5)  # Next tier
        self.t.stamp()
        self.t.sety(self.floor_level + 20)
        self.t.turtlesize(0.8, 0.3)  # Tip
        self.t.stamp()
        self.t.sety(self.floor_level)

    def get_x(self):
        return self.t.xcor()

    def get_y(self):
        return self.t.ycor()