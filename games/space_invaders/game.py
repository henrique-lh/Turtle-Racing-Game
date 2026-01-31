import random
import time
import turtle

from games.interface import Game
from games.space_invaders.constants import ALIEN_SPAWN_INTERVAL, TIME_FOR_1_FRAME
from games.space_invaders.entities import Alien, Laser, Cannon
from games.space_invaders.ui import UI


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

        self.ui.show_game_over()
        self.window.update()
        time.sleep(2)

        try:
            self.window.bye()
            turtle.bye()
        except turtle.Terminator:
            pass