import customtkinter
from frontend.components import ExitButton
from frontend.register_screen import RegisterWindow
from games import TurtleKart, SpaceInvaders
from user.user_info import Player


class GamesScreen(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("700x350")
        self.title("Hub")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.play_button = customtkinter.CTkButton(
            master=self,
            text="Play",
            command=self.list_games,
            font=customtkinter.CTkFont(size=17, family="Hack Nerd Font")
        )
        self.play_button.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        self.exit_button = ExitButton(self)
        self.exit_button.grid(row=0, column=0, padx=20, pady=10, sticky="e")

        self.games = {
            "Turtle Racing Game": TurtleKart,
            "Space Invaders": SpaceInvaders,
        }

        self.player = Player()

        self.games_frame = None
        self.register_user()

    def list_games(self):
        """
        List all available games in a grid layout
        """

        if self.games_frame:
            self.games_frame.destroy()

        self.games_frame = customtkinter.CTkScrollableFrame(
            master=self,
            width=660,
            height=250,
            corner_radius=10
        )
        self.games_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        columns = 2
        for col in range(columns):
            self.games_frame.grid_columnconfigure(col, weight=1)

        for index, (game_name, game_class) in enumerate(self.games.items()):
            row = index // columns
            col = index % columns

            button = self.create_game_button(
                master=self.games_frame,
                text=game_name,
                command=lambda g=game_class: self.play(g)
            )
            button.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")

    @staticmethod
    def create_game_button(master, text, command):
        """
        Create a custom button for each game in the list
        """

        return customtkinter.CTkButton(
            master=master,
            text=text,
            compound="center",
            command=command,
            font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"),
            height=120,
            fg_color="#1f2933",
            hover_color="#374151",
            corner_radius=15
        )

    @staticmethod
    def play(game_class):
        """
        Starts a game
        """
        game = game_class()
        game.config()
        game.play()

    def register_user(self):
        """
        Register a new player in the game
        """
        self.withdraw()
        register = RegisterWindow()
        register.wait_window()
        self.player.set_nick_name(register.nick_name)
        self.deiconify()
