import customtkinter

from games import TurtleKart, SpaceInvaders


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


def open_game(game_class):
    game = game_class()
    game.config()
    game.play()


class GamesScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("700x450")
        self.title("Hub")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Escolha seu Jogo"
        )
        self.scrollable_frame.grid(
            row=0, column=0, padx=20, pady=(20, 10), sticky="nsew"
        )

        self.scrollable_frame.grid_columnconfigure((0, 1), weight=1)

        self.games = {
            "Turtle Racing Game": TurtleKart,
            "Space Invaders": SpaceInvaders,
        }

        self.list_games()

        self.exit_button = customtkinter.CTkButton(
            self,
            text="EXIT",
            command=self.destroy,
            fg_color="transparent",
            border_width=2,
        )
        self.exit_button.grid(row=1, column=0, padx=20, pady=20)

    def list_games(self):
        row = 0
        column = 0

        for game_name, game_class in self.games.items():
            button = customtkinter.CTkButton(
                master=self.scrollable_frame,
                text=game_name,
                command=lambda g=game_class: open_game(g),
                height=100,
                font=("Hack Nerd Font", 17),
            )
            button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

            column += 1
            if column > 1:
                column = 0
                row += 1
