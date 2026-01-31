import customtkinter


class RegisterWindow(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.geometry("520x300")
        self.title("Register...")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.text_frame = customtkinter.CTkFrame(
            master=self, width=500, height=100, corner_radius=20
        )
        self.text_frame.grid(row=0, column=1, padx=20, pady=20, stick="nsew")

        self.label = customtkinter.CTkLabel(
            self.text_frame,
            text="Register",
            font=customtkinter.CTkFont(size=20, weight="bold", family="Hack Nerd Font"),
        )
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.card_entry = customtkinter.CTkEntry(
            self.text_frame,
            placeholder_text="Enter your best nick",
            height=40,
            width=280,
        )
        self.card_entry.grid(row=1, column=1, padx=20, pady=20)

        self.button = customtkinter.CTkButton(
            self,
            text="Register",
            command=self.on_click_register,
            font=customtkinter.CTkFont(size=17, family="Hack Nerd Font"),
        )
        self.button.grid(row=1, column=1, padx=20, pady=20)
        self.nick_name = ""

    def on_click_register(self):
        nick_name = self.card_entry.get()
        self.nick_name = nick_name
        self.destroy()
