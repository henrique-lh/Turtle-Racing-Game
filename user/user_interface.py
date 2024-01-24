import customtkinter
from user_info import User

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("520x350")
        self.title("Python da Sorte")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Frame para o texto
        self.text_frame = customtkinter.CTkFrame(master=self, width=500, height=200, corner_radius=20)
        self.text_frame.grid(row=0, column=1, padx=20, pady=20, stick="nsew")

        self.label = customtkinter.CTkLabel(self.text_frame, text="Realize seu registro", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.user_name_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Nome")
        self.user_name_entry.grid(row=1, column=0, padx=30, pady=20)

        self.chips_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Qt. de Fichas")
        self.chips_entry.grid(row=2, column=0, padx=30, pady=20)

        self.email_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Email")
        self.email_entry.grid(row=1, column=1, padx=20, pady=20)

        self.phone_entry = customtkinter.CTkEntry(self.text_frame, placeholder_text="Telefone")
        self.phone_entry.grid(row=2, column=1, padx=20, pady=20)

        self.button = customtkinter.CTkButton(self, text="Entrar/Registrar", command=self.save_user)
        self.button.grid(row=1, column=1, padx=20, pady=20)

    def save_user(self):
        self.user = User(self.user_name_entry.get(), int(self.chips_entry.get()), self.email_entry.get(), self.phone_entry.get())
        self.destroy()
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
    print(app.user)

