import customtkinter
from frontend import AccessOption
import csv
import os
import datetime


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


class Machine(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.geometry("700x300")
        self.title("Python da Sorte")

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Frame para o texto
        self.text_color_frame = customtkinter.CTkFrame(master=self, width=500, height=100, corner_radius=20)
        self.text_color_frame.grid(row=1, column=1, padx=20, pady=20, stick="nsew")

        self.color_label = customtkinter.CTkLabel(self, text="Faça sua aposta!", 
        font=customtkinter.CTkFont(size=20, weight="bold", family="Lato"))
        self.color_label.grid(row=0, column=1, padx=20, pady=20)

        self.color_entry = customtkinter.CTkEntry(self.text_color_frame, text_color="white", placeholder_text="Digite uma cor", height=40, width=280,
                                                  font=customtkinter.CTkFont(family="Lato"))
        self.color_entry.grid(row=1, column=0, padx=20, pady=0)
        self.color_entry.insert(0, "yellow")

        self.chip_entry = customtkinter.CTkEntry(self.text_color_frame, text_color="white", placeholder_text="Quanto deseja apostar", height=40, width=280,
                                                 font=customtkinter.CTkFont(family="Lato"))
        self.chip_entry.grid(row=1, column=1, padx=20, pady=20)
        self.chip_entry.insert(0, str(100))

        self.button_frame = customtkinter.CTkFrame(master=self, width=200, height=500, corner_radius=20)
        self.button_frame.grid(row=2, column=1, padx=20, pady=20, stick="nsew")

        self.play_button = customtkinter.CTkButton(self.button_frame, text="Jogar", command=self.play, 
                                              font=customtkinter.CTkFont(size=17, family="Lato"))
        self.play_button.place(rely=0.3, relx=0.1) 

        self.quit_button = customtkinter.CTkButton(self.button_frame, text="Sair", command=self.quit, 
                                              font=customtkinter.CTkFont(size=17, family="Lato"))
        self.quit_button.place(rely=0.3, relx=0.7)

        self.start()

    def start(self):
        self.withdraw()
        access = AccessOption()
        access.wait_window()
        self.user = access.user
        self.deiconify()

    def play(self):
        from games import TurtleKart
        user_bet = self.color_entry.get()
        game = TurtleKart()
        game.config()
        game.play(user_bet=user_bet, chips=int(self.chip_entry.get()), user=self.user)

    def quit(self):
        csv_path = os.path.join(os.path.dirname(os.path.realpath("Turtle-Racing-Game")), "results")
        csv_file = os.path.join(csv_path, "result.csv")
        with open(csv_file, mode="a", newline="") as f:
            writter = csv.writer(f)
            writter.writerow(
                [self.user.card, self.user.name, self.user.email, self.user.phone, str(self.user.total_chips), datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")]
            )
        self.destroy()


