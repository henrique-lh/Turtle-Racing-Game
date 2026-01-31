import sys
import os
import time
import random
from turtle import Turtle

import customtkinter
from CTkMessagebox import CTkMessagebox

from games.game import Game


FONT = ("Courier", 14, "bold")
ALIGN = "center"
POSITIONS = [-260, -172, -85, 2, 85, 172, 260]
FINISH_LINE = 330

DATA = [
    ("white", "#F5F5F5", "#B2B2B2", (2, 0)),
    ("red", "#F04646", "#FF0000", (2, 1)),
    ("orange", "#FF9E4D", "#FF7000", (2, 2)),
    ("pink", "#FC76FC", "#FF00D8", (3, 0)),
    ("tomato", "#FF753D", "#FF5100", (3, 1)),
    ("blue", "#7BC5FF", "#0061FF", (3, 2)),
    ("yellow", "#FFFF71", "#F7FF00", (4, 1)),
]


def display_winner(racer: Turtle, winner_name: str, user_choice: str) -> None:
    """Displays the victory or defeat message on the Turtle screen."""
    racer.goto(0, 0)

    if winner_name == user_choice:
        racer.write(f"YOU WON! The {winner_name} racer won!", font=FONT, align=ALIGN)
    else:
        racer.write(f"YOU LOST! The {winner_name} racer won!", font=FONT, align=ALIGN)


def check_finish_line(racer: Turtle, user_choice: str) -> bool:
    """Checks whether the turtle has crossed the line and displays the result."""
    if racer.xcor() > FINISH_LINE:
        winner_name = racer.color_name
        display_winner(racer, winner_name, user_choice)
        return False
    return True


class UI(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.geometry("800x500")
        self.title("Bet on your Turtle!")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.user_choice = None
        self.confirmed = False

        self.main_frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20)

        self.title_label = customtkinter.CTkLabel(
            self.main_frame,
            text="Choose a Color & Check the Odds",
            font=customtkinter.CTkFont(size=20, weight="bold", family="Hack Nerd Font")
        )
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(20, 10))

        self.odds = [round(random.randint(110, 500) / 100, 2) for _ in range(7)]

        for index, item in enumerate(DATA):
            name, hex_color, hover_color, (row, col) = item
            current_odd = self.odds[index]

            btn_row = row

            btn = customtkinter.CTkButton(
                self.main_frame,
                text=f"{name.upper()}\nOdd: {current_odd}x",
                text_color="#2A2424",
                fg_color=hex_color,
                hover_color=hover_color,
                font=customtkinter.CTkFont(size=14, weight="bold",
                                           family="Hack Nerd Font"),
                width=140,
                height=60,
                command=lambda c=name, o=current_odd: self.confirm_selection(c, o)
            )
            btn.grid(row=btn_row, column=col, padx=10, pady=10)

        self.quit_button = customtkinter.CTkButton(
            self,
            text="EXIT GAME",
            fg_color="#333333",
            hover_color="#555555",
            command=self.exit_game,
            font=customtkinter.CTkFont(size=14, weight="bold")
        )
        self.quit_button.grid(row=1, column=0, pady=20)

        self.protocol("WM_DELETE_WINDOW", self.exit_game)

    def confirm_selection(self, color_name, odd_value):
        """Opens the confirmation popup."""
        msg = CTkMessagebox(
            master=self,
            title="Confirm Bet",
            message=f"Do you want to bet on {color_name.upper()}?\nPotential Payout: {odd_value}x",
            icon="question",
            option_1="Confirm",
            option_2="Back"
        )

        response = msg.get()

        if response == "Confirm":
            self.user_choice = color_name
            self.confirmed = True
            self.destroy()
        else:
            pass

    def exit_game(self):
        """Close the entire application."""
        self.destroy()
        sys.exit()


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
        time.sleep(3)
        try:
            self.window.bye()
        except:
            pass
