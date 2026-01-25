from turtle import Turtle
import random
import os
import time

import customtkinter
from CTkMessagebox import CTkMessagebox

from games.game import Game

FONT = ("Courier", 14, "bold")
ALIGN = "right"
POSITIONS = [-260, -172, -85, 2, 85, 172, 260]
COLORS_NAME = ["white", "red", "orange", "pink", "tomato", "dodgerblue", "yellow"]
HOVER_COLORS = [
    "#B2B2B2",
    "#FF0000",
    "#FF7000",
    "#FF00D8",
    "#FF5100",
    "#0061FF",
    "#F7FF00",
]
COLORS_HEX = [
    "#F5F5F5",
    "#F04646",
    "#FF9E4D",
    "#FC76FC",
    "#FF753D",
    "#7BC5FF",
    "#FFFF71",
]
GRID = [(2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 1)]
FINISH_LINE = 330


def display_winner(racer: Turtle, winner: str, user_choice: str) -> None:
    if winner == user_choice:
        racer.write(f"You won! {winner} racer is winner", font=FONT, align=ALIGN)
    racer.write(f"You lost! The {winner} racer is winner", font=FONT, align=ALIGN)


def should_race_continue(racer: Turtle, winner: str, user_choice: str) -> bool:
    if racer.xcor() > FINISH_LINE:
        display_winner(racer, winner, user_choice)
        return False
    return True


class TurtleKart(Game):
    def __init__(self, user_turtle_choice: str) -> None:
        super().__init__()
        self.path = os.path.join(
            os.path.dirname(os.path.realpath("Turtle-Racing-Game")), "assets"
        )
        self.racers = []
        self.user_turtle_choice = user_turtle_choice

    def config(self):
        self.window.setup(width=800, height=600)
        self.window.bgpic(os.path.join(self.path, "road.gif"))

        for index in range(7):
            new_tur = Turtle(shape="turtle")
            new_tur.shapesize(2)
            new_tur.speed("fastest")
            new_tur.penup()
            new_tur.goto(x=-350, y=POSITIONS[index])
            new_tur.color(COLORS_HEX[index])
            self.racers.append(new_tur)

    def play(self):
        is_on = True
        while is_on:
            for racer in self.racers:
                is_on = should_race_continue(
                    racer=racer,
                    winner=racer.pencolor(),
                    user_choice=self.user_turtle_choice,
                )
                if not is_on:
                    break
                random_pace = random.randint(0, 30)
                racer.forward(random_pace)
        self.destroy()

    def destroy(self):
        time.sleep(1.5)
        self.window.bye()


class UI(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.geometry("1000x500")
        self.title("Kart")

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.user_bet = ""

        self.text_color_frame = customtkinter.CTkFrame(
            master=self, width=500, height=100, corner_radius=20
        )
        self.text_color_frame.grid(row=1, column=1, padx=20, pady=20, stick="nsew")

        self.color_label = customtkinter.CTkLabel(
            self,
            text="Bet it!",
            font=customtkinter.CTkFont(size=20, weight="bold", family="Hack Nerd Font"),
        )
        self.color_label.grid(row=0, column=1, padx=24, pady=20)

        self.color_entry = customtkinter.CTkTextbox(
            self.text_color_frame,
            text_color="white",
            height=40,
            width=280,
            font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"),
        )
        self.color_entry.grid(row=1, column=0, padx=20, pady=0)

        odds = [random.randint(0, 500) / 100 for _ in range(7)]

        self.odds_frame = customtkinter.CTkFrame(master=self.text_color_frame)

        self.odd_label = customtkinter.CTkLabel(
            self.text_color_frame,
            text="Odds",
            font=customtkinter.CTkFont(size=20, weight="bold", family="Hack Nerd Font"),
        )
        self.odd_label.grid(row=0, column=1, padx=20, pady=20)

        for grid, color_name, hover_color_name, hex_color, odds in zip(
            GRID, COLORS_NAME, HOVER_COLORS, COLORS_HEX, odds
        ):
            row, col = grid
            button = customtkinter.CTkButton(
                self.text_color_frame,
                text=f"{color_name.upper():<16} {odds}",
                text_color="#2A2424",
                fg_color=hex_color,
                command=lambda t=color_name: self.insert_odd_value(t),
                font=customtkinter.CTkFont(size=14, family="Hack Nerd Font"),
                hover=True,
                hover_color=hover_color_name,
            )
            button.grid(row=row, column=col, padx=5, pady=5)

        self.button_frame = customtkinter.CTkFrame(
            master=self, width=200, height=500, corner_radius=20
        )
        self.button_frame.grid(row=2, column=1, padx=20, pady=20, stick="nsew")

        self.play_button = customtkinter.CTkButton(
            self.button_frame,
            text="Play",
            command=self.play,
            font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"),
        )
        self.play_button.place(rely=0.3, relx=0.1)

        self.quit_button = customtkinter.CTkButton(
            self.button_frame,
            text="Exit",
            command=self.exit,
            font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"),
        )
        self.quit_button.place(rely=0.3, relx=0.7)
        self.game = None

    def play(self):
        if self.user_bet:
            self.game = TurtleKart(self.user_bet)
            self.game.config()
            self.game.play()
        else:
            no_bet_color = CTkMessagebox(
                master=self,
                title="Error",
                message="Please, choose a color!",
                option_1="Continue",
            )
            no_bet_color.wait_window()

    def exit(self):
        if self.game is not None:
            self.game.screen.bye()
        self.destroy()

    def insert_odd_value(self, text):
        self.color_entry.delete("1.0", customtkinter.END)
        self.color_entry.insert("1.0", text)
        self.user_bet = text
