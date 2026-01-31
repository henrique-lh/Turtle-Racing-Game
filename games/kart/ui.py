import random
import sys

import customtkinter
from CTkMessagebox import CTkMessagebox

from games.kart.constants import DATA


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
