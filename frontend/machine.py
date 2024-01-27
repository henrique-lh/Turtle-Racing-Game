import customtkinter
from games import TurtleKart
from frontend import AccessOption, ChipsOptions
import csv
import os
import datetime
import pytz
import random
from CTkMessagebox import CTkMessagebox


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


class Machine(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.geometry("1000x500")
        self.title("Python da Sorte")

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.user_bet = ""

        # Frame para o texto
        self.text_color_frame = customtkinter.CTkFrame(master=self, width=500, height=100, corner_radius=20)
        self.text_color_frame.grid(row=1, column=1, padx=20, pady=20, stick="nsew")

        self.color_label = customtkinter.CTkLabel(self, text="Faça sua aposta!", 
                                                  font=customtkinter.CTkFont(size=20, weight="bold", family="Hack Nerd Font"))
        self.color_label.grid(row=0, column=1, padx=24, pady=20)

        self.color_entry = customtkinter.CTkTextbox(self.text_color_frame, text_color="white", 
                                                    height=40, width=280, font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"))
        self.color_entry.grid(row=1, column=0, padx=20, pady=0)

        self.chip_entry = customtkinter.CTkEntry(self.text_color_frame, text_color="white", placeholder_text="Quanto deseja apostar", height=40, width=280,
                                                 font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"))
        self.chip_entry.grid(row=1, column=2, padx=20, pady=20)
        self.chip_entry.insert(0, str(100))

        self.text_colors = ["white", "red", "orange", "pink", "tomato", "dodgerblue", "yellow"]
        hover_colors = ["#B2B2B2", "#FF0000", "#FF7000", "#FF00D8", "#FF5100", "#0061FF", "#F7FF00"]
        colors = ["#F5F5F5", "#F04646", "#FF9E4D", "#FC76FC", "#FF753D", "#7BC5FF", "#FFFF71"]
        self.values = [random.randint(0, 500) / 100 for _ in range(7)]
        positions = [
            (2, 0), (2, 1), (2, 2),
            (3, 0), (3, 1), (3, 2),
            (4, 1)
        ]

        self.odds_frame = customtkinter.CTkFrame(master=self.text_color_frame)

        self.odd_label = customtkinter.CTkLabel(self.text_color_frame, text="Odds!", 
                                                  font=customtkinter.CTkFont(size=20, weight="bold", family="Hack Nerd Font"))
        self.odd_label.grid(row=0, column=1, padx=20, pady=20)

        for pos, text, hover, color, value in zip(positions, self.text_colors, hover_colors, colors, self.values):
            row, col = pos
            button = customtkinter.CTkButton(self.text_color_frame, text=f"{text.upper():<16} {value}", 
                                             text_color="#2A2424", fg_color=color, command=lambda t = text: self.show_value(t),
                                             font=customtkinter.CTkFont(size=14, family="Hack Nerd Font"), hover=True, hover_color=hover)
            button.grid(row=row, column=col, padx=5, pady=5)
        # acabou

        self.button_frame = customtkinter.CTkFrame(master=self, width=200, height=500, corner_radius=20)
        self.button_frame.grid(row=2, column=1, padx=20, pady=20, stick="nsew")

        self.play_button = customtkinter.CTkButton(self.button_frame, text="Jogar", command=self.play, 
                                              font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"))
        self.play_button.place(rely=0.3, relx=0.1)

        self.quit_button = customtkinter.CTkButton(self.button_frame, text="Sair", command=self.quit, 
                                              font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"))
        self.quit_button.place(rely=0.3, relx=0.7)

        self.start()

    def start(self):
        self.withdraw()
        access = AccessOption()
        access.wait_window()
        self.user = access.user
        self.deiconify()
        self.total_chips_text = customtkinter.CTkLabel(self.button_frame, text=f"Fichas: {self.user.total_chips}",
                                                       font=customtkinter.CTkFont(size=20, family="Hack Nerd Font"))
        self.total_chips_text.place(rely=0.3, relx=0.4)

    def play(self):
        if self.user_bet:
            try:
                bet_chips = int(self.chip_entry.get())
                self.user.bet(bet_chips)
                self.game = TurtleKart()
                self.total_chips_text.configure(text=f"Fichas: {self.user.total_chips}")    # Após aposta, antes do resultado
                self.game.config(self.text_colors, self.values)
                self.game.play(user_bet=self.user_bet, chips=bet_chips, user=self.user)
                self.total_chips_text.configure(text=f"Fichas: {self.user.total_chips}")    # Após resultado
            except ValueError as e:
                self.withdraw()
                no_chips_message = CTkMessagebox(
                    master=self, title="Valor insuficiente", message=f"Você não possui fichas o suficiente! Suas fichas {self.user.total_chips}", 
                    icon="warning", option_1="Adicionar mais fichas", option_2="Sair"
                )
                if no_chips_message.get() == "Sair":
                    self.quit()
                chips_option = ChipsOptions()
                chips_option.wait_window()
                self.user.total_chips += chips_option.added_chips
                self.deiconify()
        else:
            no_bet_color = CTkMessagebox(master=self, title="Erro", message="Por favor, escolha uma cor", option_1="Continuar")
            no_bet_color.wait_window()

    def quit(self):
        csv_path = os.path.join(os.path.dirname(os.path.realpath("Turtle-Racing-Game")), "results")
        csv_file = os.path.join(csv_path, "result.csv")
        time_format = "%d/%m/%Y - %H:%M".strip()
        timezone = pytz.timezone("America/Recife")
        with open(csv_file, mode="a", newline="") as f:
            writter = csv.writer(f)
            writter.writerow(
                [self.user.card, self.user.name, self.user.email, self.user.phone, str(round(self.user.total_chips, 2)), datetime.datetime.now(timezone).strftime(time_format)]
            )
        self.destroy()
        self.game.screen.bye()

    def show_value(self, text):
        self.color_entry.delete("1.0", customtkinter.END)
        self.color_entry.insert("1.0", text)
        self.user_bet = text

