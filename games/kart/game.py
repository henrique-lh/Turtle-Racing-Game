import os
import random
import sys
import time
from turtle import Turtle

from games.interface import Game
from games.kart.constants import DATA, POSITIONS
from games.kart.ui import UI
from games.kart.utils import check_finish_line


class TurtleKart(Game):
    def __init__(self) -> None:
        super().__init__()
        self.assets_path = os.path.join(
            os.path.dirname(os.path.realpath("Turtle-Racing-Game")), "assets"
        )

        self.racers = []
        self.user_choice = ""

    def config(self):
        ui = UI()
        ui.wait_window()

        if not ui.confirmed or not ui.user_choice:
            sys.exit()

        self.user_choice = ui.user_choice

        self.window.setup(width=800, height=600)
        self.window.title(f"Turtle Racing - Betting on: {self.user_choice.upper()}")

        bg_image = os.path.join(self.assets_path, "road.gif")
        if os.path.exists(bg_image):
            self.window.bgpic(bg_image)
        else:
            self.window.bgcolor("forestgreen")

        for index, item in enumerate(DATA):
            name, hex_color, _, _ = item

            new_tur = Turtle(shape="turtle")
            new_tur.shapesize(2)
            new_tur.speed("fastest")
            new_tur.penup()
            new_tur.goto(x=-350, y=POSITIONS[index])
            new_tur.color(hex_color)

            new_tur.color_name = name

            self.racers.append(new_tur)

    def play(self):
        is_on = True
        while is_on:
            for racer in self.racers:
                is_on = check_finish_line(racer, self.user_choice)

                if not is_on:
                    break

                random_pace = random.randint(0, 10)
                racer.forward(random_pace)

        self.cleanup()

    def cleanup(self):
        time.sleep(2)
        try:
            self.window.bye()
        except:
            pass
