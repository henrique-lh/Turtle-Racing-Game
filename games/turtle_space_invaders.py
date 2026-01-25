import random
import time
import turtle

from games.game import Game


FRAME_RATE = 30
TIME_FOR_1_FRAME = 1 / FRAME_RATE
CANNON_STEP = 10
LASER_LENGTH = 20
LASER_SPEED = 20
ALIEN_SPAWN_INTERVAL = 1.2
ALIEN_SPEED = 3.5


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


class UI:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.color(1, 1, 1)

    def update_score(self, time_elapsed, score, x, y):
        self.pen.clear()
        self.pen.setposition(x, y)
        self.pen.write(
            f"Time: {time_elapsed:5.1f}s\nScore: {score:5}",
            font=("Courier", 20, "bold"),
        )

    def show_game_over(self):
        self.pen.home()
        self.pen.write("GAME OVER", font=("Courier", 40, "bold"), align="center")


class SpaceInvaders(Game):
    def __init__(self):
        super().__init__()
        self.lasers = []
        self.aliens = []
        self.score = 0
        self.game_timer = 0
        self.alien_timer = 0

        self.width = self.window.window_width()
        self.height = self.window.window_height()
        self.left = -self.width / 2
        self.right = self.width / 2
        self.top = self.height / 2
        self.bottom = -self.height / 2
        self.floor = 0.9 * self.bottom
        self.gutter = 0.025 * self.width

        self.cannon = Cannon(0, self.floor, self.floor)
        self.ui = UI()

    def config(self):
        self.window.tracer(0)
        self.window.setup(0.5, 0.75)
        self.window.bgcolor(0.2, 0.2, 0.2)
        self.window.title("Space Invaders")

        self.window.onkeypress(lambda: self.cannon.change_direction(-1), "Left")
        self.window.onkeypress(lambda: self.cannon.change_direction(1), "Right")
        self.window.onkeyrelease(lambda: self.cannon.change_direction(0), "Left")
        self.window.onkeyrelease(lambda: self.cannon.change_direction(0), "Right")
        self.window.onkeypress(self.fire_laser, "space")
        self.window.onkeypress(self.window.bye, "q")
        self.window.listen()

    def fire_laser(self):
        self.lasers.append(Laser(self.cannon.get_x(), self.cannon.get_y()))

    def spawn_alien(self):
        if time.time() - self.alien_timer > ALIEN_SPAWN_INTERVAL:
            x_pos = random.randint(
                int(self.left + self.gutter), int(self.right - self.gutter)
            )
            self.aliens.append(Alien(x_pos, self.top))
            self.alien_timer = time.time()

    def check_collisions(self):
        for laser in self.lasers[:]:
            laser.move()

            if laser.get_y() > self.top:
                laser.cleanup()
                self.lasers.remove(laser)
                continue

            for alien in self.aliens[:]:
                if (
                    abs(laser.get_pos()[0] - alien.get_pos()[0]) < 20
                    and abs(laser.get_pos()[1] - alien.get_pos()[1]) < 20
                ):
                    laser.cleanup()
                    alien.cleanup()
                    if laser in self.lasers:
                        self.lasers.remove(laser)
                    if alien in self.aliens:
                        self.aliens.remove(alien)
                    self.score += 1
                    break

    def update_aliens(self):
        for alien in self.aliens:
            alien.move()
            if alien.get_y() < self.floor:
                self.game_running = False

    def play(self):
        self.cannon.draw()
        self.game_running = True
        self.game_timer = time.time()

        try:
            while self.game_running:
                timer_this_frame = time.time()

                time_elapsed = time.time() - self.game_timer
                self.ui.update_score(
                    time_elapsed, self.score, self.left * 0.8, self.top * 0.8
                )

                self.cannon.update_position(
                    self.left + self.gutter, self.right - self.gutter
                )

                self.spawn_alien()
                self.check_collisions()
                self.update_aliens()

                time_for_this_frame = time.time() - timer_this_frame
                if time_for_this_frame < TIME_FOR_1_FRAME:
                    time.sleep(TIME_FOR_1_FRAME - time_for_this_frame)

                self.window.update()
        except turtle.Terminator:
            self.game_running = False
            return

        self.ui.show_game_over()

        try:
            self.window.bye()
            turtle.bye()
        except turtle.Terminator:
            pass